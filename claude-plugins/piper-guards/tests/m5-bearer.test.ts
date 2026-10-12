import { expect, test } from 'claude-code/testing'
import { guardedPath } from '../hooks/register.js'

const R = '/Users/xian/Development/piper-morgan-worktrees/cio'
const run = (stdout: string, exitCode = 0) => ({ exitCode, stdout, stderr: '', isStdoutTruncated: false, isStderrTruncated: false })

test('M-5 scopes to mailboxes/, docs/, dev/', async () => {
  expect(guardedPath(R + '/mailboxes/exec/inbox/m.md')?.root).toBe(R)
  expect(guardedPath(R + '/docs/a.md')?.rel).toBe('docs/a.md')
  expect(guardedPath(R + '/dev/2026/10/12/log.md')?.rel).toBe('dev/2026/10/12/log.md')
  expect(guardedPath(R + '/services/a.py')).toBe(null)
  expect(guardedPath('/Users/xian/Development/x.md')).toBe(null)
})

// The linter itself is stubbed here (exit 1 plus its FAIL line); its detection has its own tests in the repo.
test('M-5 hook denies on a linter hit, allows on a clean run, fails open without the script', async ($, on) => {
  let result = run('mailbox_bearer_lint: FAIL - 1 bearer credential(s) in repo-committed text (#1845):\n  /tmp/x.md:1  ABCD...WXYZ\n', 1)
  let hasScript = true
  on('session.cwd', () => ({ value: R }))
  on('fs.exists', () => ({ value: hasScript }))
  on('fs.write', () => ({ value: undefined }))
  on('process.run', () => ({ value: result }))
  on('tool.call', () => ({ result: 'ran' }))
  const w = { tool: 'Write', file_path: R + '/mailboxes/exec/inbox/m.md', content: 'hello' }
  const denied: any = await $.tool.call(w)
  expect(denied.deny).toMatch(/BLOCKED by piper-guards M-5/)
  const edited: any = await $.tool.call({ tool: 'Edit', file_path: R + '/docs/a.md', old_string: 'a', new_string: 'b' })
  expect(edited.deny).toMatch(/M-5/)
  expect(await $.tool.call({ tool: 'Write', file_path: R + '/services/a.py', content: 'x' })).toEqual({ result: 'ran' })
  result = run('mailbox_bearer_lint: OK', 0)
  expect(await $.tool.call(w)).toEqual({ result: 'ran' })
  result = run('', 1)
  expect(await $.tool.call(w)).toEqual({ result: 'ran' })
  hasScript = false
  result = run('mailbox_bearer_lint: FAIL bearer credential', 1)
  expect(await $.tool.call(w)).toEqual({ result: 'ran' })
})
