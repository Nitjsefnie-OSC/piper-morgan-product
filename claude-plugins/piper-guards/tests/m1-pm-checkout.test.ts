import { expect, test } from 'claude-code/testing'
import { findViolations } from '../hooks/register.js'

const PM = '/Users/xian/Development/piper-morgan-product'
const WT = '/Users/xian/Development/piper-morgan-worktrees/cio'
const H = '/Users/xian'
const v = (cmd: string, cwd = WT) => findViolations(cmd, cwd, PM, H).length

// Unit cases, mirroring guard_pm_checkout.py's rules.
test('blocks destructive git aimed at the PM checkout', async () => {
  expect(v('git -C ' + PM + ' checkout -- .')).toBe(1)
  expect(v('cd ' + PM + ' && git reset --hard origin/main')).toBe(1)
  expect(v('git stash', PM)).toBe(1)
  expect(v('git stash -u', PM + '/docs')).toBe(1)
  expect(v('git restore README.md', PM)).toBe(1)
  expect(v('git clean -fd', PM)).toBe(1)
  expect(v('git checkout origin/main -- docs/x.md', PM)).toBe(1)
  expect(v('cd ~/Development/piper-morgan-product; git checkout .')).toBe(1)
  expect(v('git -c core.x=y -C ' + PM + ' stash pop')).toBe(1)
})

test('allows safe git, and anything in a worktree', async () => {
  expect(v('git status', PM)).toBe(0)
  expect(v('git stash list', PM)).toBe(0)
  expect(v('git restore --staged x', PM)).toBe(0)
  expect(v('git checkout -- .', WT)).toBe(0)
  expect(v('git reset --hard', WT)).toBe(0)
  expect(v('git -C ' + WT + ' stash', PM)).toBe(0)
  expect(v('git log --oneline -3', PM)).toBe(0)
  expect(v('echo "git reset --hard"', PM)).toBe(0)
  expect(v('cd ' + PM + ' && cd ' + WT + ' && git checkout -- .')).toBe(0)
  expect(v('git -C ' + PM + '-other reset --hard')).toBe(0)
})

// Through the engine: the mod's tool.call hook denies before Claude Code runs anything.
test('the hook denies in PM checkout and passes elsewhere', async ($, on) => {
  let cwd = PM
  on('session.cwd', () => ({ value: cwd }))
  on('tool.call', () => ({ result: 'ran' }))
  const denied: any = await $.tool.call({ tool: 'Bash', command: 'git reset --hard' })
  expect(denied.deny).toMatch(/BLOCKED by piper-guards M-1/)
  cwd = WT
  expect(await $.tool.call({ tool: 'Bash', command: 'git reset --hard' })).toEqual({ result: 'ran' })
  expect(await $.tool.call({ tool: 'Bash', command: 'ls -la' })).toEqual({ result: 'ran' })
  expect(await $.tool.call({ tool: 'Read', file_path: '/x' })).toEqual({ result: 'ran' })
})
