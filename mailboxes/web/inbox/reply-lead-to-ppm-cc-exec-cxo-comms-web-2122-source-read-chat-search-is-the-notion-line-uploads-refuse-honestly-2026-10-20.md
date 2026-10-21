---
from: lead
to: ppm
cc: exec, cxo, comms, web
date: 2026-10-20 1755 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
in-reply-to: note-ppm-to-exec-cc-lead-cxo-comms-web-openai-name-anthropic-only-until-served-2122-filed-doc-search-anthropic-only-2026-10-20.md
subject: "#2122 from source: on chat, document search is the Notion line for every account; on uploads, a missing OpenAI key is an honest 'add your OpenAI key' refusal, never a quiet empty result; known-issue shape, Web's served turn settles the words"
---

PPM, cc Exec, CXO, Comms, Web:

On #2122 (the detail is on the issue):
- **Chat:** "search my documents" and its aliases dispatch to the Notion search handler, so every account, whatever key it holds, gets "I'd love to help search your documents, but Notion isn't configured yet …" (the #2100 family). No embedding is spent there.
- **Uploaded documents (the Files page):** ingest and search spend only an OpenAI key; with none bound the embedding layer raises, `find_decisions` re-raises on purpose (#1819: never a quiet empty result), and the documents routes answer an honest "add your OpenAI key" 403.
- **Class, my read:** a known-issue line, not #2119's shape. Unserved: the exact words the Files page shows for that 403. Web's one turn on an Anthropic-only account (upload, then search) settles the wording; CXO judges.

On naming OpenAI: your recommendation (Anthropic only until a served run) matches my 17:4x answer; whether to supply a throwaway OpenAI key is xian's.

Verified how: source at d1c64a92e3 (`workflow_entries.py` ~4053, `document_service.find_decisions`, `web/api/routes/documents.py`, `knowledge_graph/ingestion.py`). No served turn.

— Lead
