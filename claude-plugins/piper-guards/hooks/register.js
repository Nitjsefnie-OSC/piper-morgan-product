// piper-guards — R6 step 6 (stage 7 of dev/2026/10/03/spec-eval/D-propose-ruleset.md). CIO, 2026-10-12.
//
// M-1, ported from .claude/hooks/guard_pm_checkout.py (same rules, same messages): refuse git commands that
// discard working-tree state when they target PM's main checkout. PM edits there without committing, so the
// discarded changes are unrecoverable (CLAUDE.md HARD RULE). Target = `git -C <dir>` if given, else the last
// `cd <dir>` earlier in the command, else the session cwd.
//
// Fails OPEN on its own error (the .catch passes the call on): a bug here must never wedge a seat's ordinary
// work, and the settings hook (guard-pm-checkout.sh) still runs behind it during the parallel week.
// Cost: string parsing per Bash call, no subprocess. Benefit: none yet: measuring (prevention guard).
// Review: 2026-12-01. Owner: CIO.

export function splitSegments(cmd) {
  return cmd.split(/&&|\|\||;|\n|\|/)
}

// Minimal POSIX-ish tokenizer: handles '…', "…" and backslash escapes; good enough for git argv.
export function tokenize(seg) {
  const out = []
  let cur = null
  let q = null
  for (let i = 0; i < seg.length; i++) {
    const c = seg[i]
    if (q) {
      if (c === q) q = null
      else if (c === '\\' && q === '"' && i + 1 < seg.length) cur += seg[++i]
      else cur += c
      continue
    }
    if (c === "'" || c === '"') { q = c; if (cur === null) cur = ''; continue }
    if (c === '\\' && i + 1 < seg.length) { cur = (cur ?? '') + seg[++i]; continue }
    if (/\s/.test(c)) { if (cur !== null) { out.push(cur); cur = null } continue }
    cur = (cur ?? '') + c
  }
  if (cur !== null) out.push(cur)
  return out
}

function norm(p) {
  const parts = []
  for (const s of p.split('/')) {
    if (s === '' || s === '.') continue
    if (s === '..') parts.pop()
    else parts.push(s)
  }
  return '/' + parts.join('/')
}

export function resolve(p, base, home) {
  let x = p
  if (x === '~' || x.startsWith('~/')) x = home + x.slice(1)
  return norm(x.startsWith('/') ? x : base + '/' + x)
}

// Returns [{seg, why}] for every segment that would discard state in PM's checkout.
export function findViolations(cmd, cwd, pm, home) {
  const isPm = (p) => p === pm || p.startsWith(pm + '/')
  let base = cwd
  const bad = []
  for (const seg of splitSegments(cmd)) {
    const toks = tokenize(seg)
    if (!toks.length) continue
    if (toks[0] === 'cd' && toks.length > 1) { base = resolve(toks[1], base, home); continue }
    const gi = toks.indexOf('git')
    if (gi < 0) continue
    let rest = toks.slice(gi + 1)
    let tgt = base
    while (rest.length && rest[0].startsWith('-')) {
      if (rest[0] === '-C' && rest.length > 1) { tgt = resolve(rest[1], tgt, home); rest = rest.slice(2); continue }
      if (rest[0] === '-c' && rest.length > 1) { rest = rest.slice(2); continue }
      rest = rest.slice(1)
    }
    if (!rest.length || !isPm(tgt)) continue
    const sub = rest[0]
    const args = rest.slice(1)
    let why = null
    if (sub === 'checkout' && (args.includes('--') || args.includes('.'))) why = 'checkout overwrites working-tree files'
    else if (sub === 'restore' && !args.includes('--staged') && !args.includes('-S')) why = 'restore (without --staged) overwrites working-tree files'
    else if (sub === 'reset' && args.includes('--hard')) why = 'reset --hard discards working-tree changes'
    else if (sub === 'clean' && args.some((a) => a.startsWith('-') && (a.includes('f') || a.includes('x')))) why = 'clean deletes untracked files'
    else if (sub === 'stash' && !(args.length && (args[0] === 'list' || args[0] === 'show'))) why = 'stash removes working-tree changes (and the stack is shared)'
    if (why) bad.push({ seg: seg.trim(), why })
  }
  return bad
}

export function denyMessage(bad, pm) {
  const lines = bad.map((b) => `BLOCKED by piper-guards M-1 (R6): \`${b.seg}\` targets PM's main checkout (${pm}): ${b.why}.`)
  lines.push("PM edits there without committing; discarded changes are unrecoverable (CLAUDE.md HARD RULE).")
  lines.push('Do the work from your own worktree instead. If PM explicitly asked for this, PM runs it.')
  return lines.join('\n')
}

export function register(on, options) {
  const pm = norm(options.pm_checkout || '/Users/xian/Development/piper-morgan-product')
  on('tool.call', { tool: 'Bash' }, async ($, e, next) => {
    const cmd = String(e.command ?? '')
    if (!cmd.includes('git')) return next(e)
    const cwd = norm(String(await $.session.cwd()))
    const home = cwd.match(/^\/Users\/[^/]+/)?.[0] || '/Users/xian'
    const bad = findViolations(cmd, cwd, pm, home)
    if (bad.length) return { deny: denyMessage(bad, pm) }
    return next(e)
  }).catch(async ($, e, next) => next(e))
}
