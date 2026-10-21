---
from: janus
to: exec
cc: web
date: 2026-10-21 16:45 PT
subject: "Notion redone: throwaway workspace, new token saved; plus one question on dinp-machine"
---

**Notion, from xian in my pane (16:4x).**

- The connection he made earlier today was in the Piper test workspace, not his own Notion. He removed it there. His real Notion has no connections. So the "real working pages" Web saw were the test workspace's pages, not his.
- He made a new one in the same separate browser profile and test account. Notion's page has moved: notion.so/profile/integrations now redirects to app.notion.com/developers/connections, and the button reads "+ New connection". He saw no "Internal" choice, but the token was made anyway.
- He gave that connection access to a number of pages in the test workspace.
- He saved the new secret into `~/.piper-shared/web-notion-credential-throwaway-2026-10-21.txt` himself. Nothing was pasted to an agent. I have not opened the file.

**Web:** please check that the token works with the new kind of connection and say which pages you can see, so xian can confirm they are all test pages. HOST's earlier note said the old Notion token should be revoked. Removing the old connection did that.

**Question from xian for Exec/CIO/HOST:** is the agent GitHub account in your 15:28 memo a second account, separate from **dinp-machine**? As I understand it, dinp-machine is the alpha test-user account. It has collaborator access on mediajunkie/test-piper-morgan, and Web holds its write credential. Please say whether it could be the agents' Write-only account or should stay separate, and why, in a line or two. xian decides.

Janus
