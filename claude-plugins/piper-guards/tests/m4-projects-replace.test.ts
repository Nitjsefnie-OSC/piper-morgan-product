import { expect, test } from 'claude-code/testing'
import { isProjectsFullReplace } from '../hooks/register.js'

test('M-4 flags a single-select option-list write', async () => {
  expect(isProjectsFullReplace(`gh api graphql -f query='mutation { updateProjectV2Field(input: {fieldId: "F", singleSelectOptions: [{name: "S1"}]}) { projectV2Field { id } } }'`)).toBe(true)
  expect(isProjectsFullReplace('gh api graphql -F query=@q.graphql # updateProjectV2Field singleSelectOptions')).toBe(true)
})

test('M-4 leaves other Projects calls alone', async () => {
  expect(isProjectsFullReplace(`gh api graphql -f query='mutation { updateProjectV2ItemFieldValue(input: {value: {singleSelectOptionId: "x"}}) { projectV2Item { id } } }'`)).toBe(false)
  expect(isProjectsFullReplace(`gh api graphql -f query='query { node(id: "P") { ... on ProjectV2 { fields(first: 20) { nodes { ... on ProjectV2SingleSelectField { options { id name } } } } } } }'`)).toBe(false)
  expect(isProjectsFullReplace('grep -rn updateProjectV2Field singleSelectOptions docs/')).toBe(false)
})

test('the hook denies M-4 before Claude Code runs it', async ($, on) => {
  on('session.cwd', () => ({ value: '/Users/xian/Development/piper-morgan-worktrees/cio' }))
  on('tool.call', () => ({ result: 'ran' }))
  const r: any = await $.tool.call({ tool: 'Bash', command: `gh api graphql -f query='mutation { updateProjectV2Field(input: {singleSelectOptions: []}) { x } }'` })
  expect(r.deny).toMatch(/BLOCKED by piper-guards M-4/)
  expect(await $.tool.call({ tool: 'Bash', command: 'gh issue list' })).toEqual({ result: 'ran' })
})
