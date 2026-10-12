import { expect, test } from 'claude-code/testing'
import { statusText } from '../hooks/register.js'

test('M-9 status text', async () => {
  expect(statusText({ ci: 'red', briefingDays: 5 })).toBe('CI main: red · briefing 5d')
  expect(statusText({ ci: undefined, briefingDays: 0 })).toBe('briefing 0d')
  expect(statusText({ ci: undefined, briefingDays: undefined })).toBe(undefined)
})
