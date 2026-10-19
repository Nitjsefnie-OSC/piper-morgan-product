import { expect, test } from 'claude-code/testing'
import { ciVerdict, mainCiSummary, statusText } from '../hooks/register.js'

test('M-9 status text', async () => {
  expect(statusText({ ci: 'red', briefingDays: 5 })).toBe('CI main: red · briefing 5d')
  expect(statusText({ ci: undefined, briefingDays: 0 })).toBe('briefing 0d')
  expect(statusText({ ci: undefined, briefingDays: undefined })).toBe(undefined)
})

test('M-9 CI verdict: per workflow, newest success/failure; never a run status', async () => {
  const W = (workflowName, conclusion) => ({ workflowName, conclusion })
  expect(ciVerdict([W('Tests', 'skipped'), W('Tests', 'success'), W('Lint', 'success')])).toBe('green')
  expect(ciVerdict([W('Tests', 'cancelled'), W('Tests', 'failure'), W('Lint', 'success'), W('Tests', 'success')])).toBe('red (1 of 2)')
  expect(ciVerdict([W('Tests', ''), W('Lint', 'skipped')])).toBe(undefined)
  expect(ciVerdict([])).toBe(undefined)
})

test('M-9 reads main-ci-status.sh\'s summary line', async () => {
  expect(mainCiSummary('x\nmain-ci-status: 12 workflows: 11 green, 1 red, 0 unmeasured\n')).toBe('red (1 of 12)')
  expect(mainCiSummary('main-ci-status: 12 workflows: 12 green, 0 red, 0 unmeasured')).toBe('green')
  expect(mainCiSummary('main-ci-status: 12 workflows: 11 green, 0 red, 1 unmeasured')).toBe('green (11 of 12)')
  expect(mainCiSummary('gh: not logged in')).toBe(undefined)
})
