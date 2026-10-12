import { expect, test } from 'claude-code/testing'
import { checkoutFromRef, hasDiffReviewed } from '../hooks/register.js'

const WT = '/Users/xian/Development/piper-morgan-worktrees/cio'
const H = '/Users/xian'
const hits = (cmd: string) => checkoutFromRef(cmd, WT, H)

test('M-2 parses checkout-from-ref and restore --source', async () => {
  expect(hits('git checkout origin/main -- docs/x.md')).toEqual([{ seg: 'git checkout origin/main -- docs/x.md', dir: WT, paths: ['docs/x.md'] }])
  expect(hits('git restore --source=origin/main a.md b.md')[0].paths).toEqual(['a.md', 'b.md'])
  expect(hits('git restore -s HEAD~1 a.md')[0].paths).toEqual(['a.md'])
  expect(hits('git -C /tmp/r checkout HEAD -- f')[0].dir).toBe('/tmp/r')
})

test('M-2 ignores other git', async () => {
  expect(hits('git checkout main')).toEqual([])
  expect(hits('git checkout -b feature')).toEqual([])
  expect(hits('git restore --staged a.md')).toEqual([])
  expect(hits('git status')).toEqual([])
  expect(hasDiffReviewed('git checkout x -- f # diff-reviewed')).toBe(true)
  expect(hasDiffReviewed('git checkout x -- f')).toBe(false)
})

const run = (stdout: string, exitCode = 0) => ({ exitCode, stdout, stderr: '', isStdoutTruncated: false, isStderrTruncated: false })

test('M-2 hook denies with the stat, allows when clean or reviewed', async ($, on) => {
  let out = ' a.md | 2 +-\n 1 file changed\n'
  on('session.cwd', () => ({ value: WT }))
  on('process.run', () => ({ value: run(out) }))
  on('tool.call', () => ({ result: 'ran' }))
  const denied: any = await $.tool.call({ tool: 'Bash', command: 'git checkout origin/main -- a.md' })
  expect(denied.deny).toMatch(/BLOCKED by piper-guards M-2/)
  expect(denied.deny).toMatch(/a\.md \| 2/)
  expect(denied.deny).toMatch(/diff-reviewed/)
  expect(await $.tool.call({ tool: 'Bash', command: 'git checkout origin/main -- a.md # diff-reviewed' })).toEqual({ result: 'ran' })
  out = ''
  expect(await $.tool.call({ tool: 'Bash', command: 'git checkout origin/main -- a.md' })).toEqual({ result: 'ran' })
})
