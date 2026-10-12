import { expect, test } from 'claude-code/testing'

test('M-6 denies an Agent call with no model, allows one that sets it', async ($, on) => {
  on('session.cwd', () => ({ value: '/tmp' }))
  on('tool.call', () => ({ result: 'ran' }))
  const denied: any = await $.tool.call({ tool: 'Agent', description: 'd', prompt: 'p' })
  expect(denied.deny).toMatch(/BLOCKED by piper-guards M-6/)
  expect(denied.deny).toMatch(/haiku/)
  expect(await $.tool.call({ tool: 'Agent', description: 'd', prompt: 'p', model: 'sonnet' })).toEqual({ result: 'ran' })
  expect(await $.tool.call({ tool: 'Agent', description: 'd', prompt: 'p', model: 'haiku' })).toEqual({ result: 'ran' })
  // a fork can't take model (it always inherits), so it passes without one
  expect(await $.tool.call({ tool: 'Agent', description: 'd', prompt: 'p', subagent_type: 'fork' })).toEqual({ result: 'ran' })
  expect((await $.tool.call({ tool: 'Agent', description: 'd', prompt: 'p', subagent_type: 'general-purpose' }) as any).deny).toMatch(/M-6/)
})
