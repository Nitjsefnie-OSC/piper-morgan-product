# S5: GitHub reads with the Alpha app revoked (#1965, #1889, plus #2012's Test)

**Owner**: PA, run by xian. **Written** 2026-10-15 09:48 from the code on main (Lead's landing `4a39c01ce2`).
**PASSED 10-15 16:19 on `6f2916d10f`** (comment on #1965). **Re-run steps 3–4 now: alpha serves `6bb955919d`** (promoted 10-16 07:45; carries #2029 and #2031; verified with `git merge-base --is-ancestor`). **What it still decides (10-16 08:26):** #2031's no-token Integrations card. #2029, #2037 and #2012 closed on Web's stale-plus-PAT run; your Settings card and Reconnect are a second look at the no-token case. Do the reads (step 3.1) before looking at the cards: a grant is marked stale only when a read gets GitHub's 401.
About 10 minutes.

**Why**: on 10-14, with the Alpha app revoked, all four reads still said "no open issues" (4 of 4 FAIL). Lead's fix
makes a revoked grant read as a broken connection. This run shows it on the served app.

## 1. Before (the connection is good)
On alpha, signed in as yourself, run the read snippet below in the browser console. Expect `degraded []` and
your real issues.

## 2. Break it
GitHub → Settings → Applications → **Authorized OAuth Apps** → **Piper Morgan Alpha** → Revoke.

## 3. The four reads, plus the Test
1. Run the read snippet again. **Pass**: `degraded` lists github with `stale_token`; `today`, `slack` and
   `markdown` say GitHub couldn't be read and to reconnect. **No** "no open issues" or ✅ for GitHub.
2. Settings → Integration Health → GitHub → **Test** (on the next build, look at the card first: **Pass** = ⚠️
   "Needs reconnecting", "GitHub no longer accepts your connection.", a **Reconnect** button, no Test button (if it says ⚠️ "Connected via your personal token" instead, your account also holds a PAT: that covers #2037's amber icon, so screenshot it)
   (#2031). Never "Not configured" or "Connected"). On `6f2916d10f`: **Pass**: it fails, and says to reconnect. (On 10-14 it
   said "connection successful".) CXO judges the wording.
3. Open Settings → GitHub (`/settings/integrations/github`; from 6bb955919d `/settings/github` redirects there, #2039) and note what it says. **Depends on the build** (check alpha `/health`):
   - on `6f2916d10f` (today's): it still says ✅ Connected with no Connect button (#2029, a known gap, not an S5
     failure; a screenshot helps).
   - on `6bb955919d` (served from 10-16 07:45; #2029 `bee366050c`, #2031 `af593e58e2`): **Pass** = ⚠️ "Needs reconnecting", "GitHub no longer
     accepts your connection, so I can't read your GitHub right now.", and a **Reconnect with GitHub** button.
     Never "Connected".

## 4. Reconnect
- **On `6bb955919d`:** click **Reconnect with GitHub** on Settings → GitHub. One step, no Disconnect (Lead
  10-15: a re-grant updates the stale connection in place). **Pass**: back to ✅ Connected. Reload the Integrations
  page before judging its card: Web saw it keep stale words after a Test until a reload (10-16, finding 2).
- **On `6f2916d10f`:** Integrations → GitHub → **Disconnect** → confirm, then **Connect with GitHub** (#2017's
  fix is live). If Disconnect still does nothing, use the console fallback below and tell PA.

## 5. After
Run the read snippet once more. **Pass**: `degraded []` and your issues are back.

Paste each console output to PA (or into the PA chat). PA relays the readings to Lead and CXO and comments on
#1965, #1889, #2012, #2017, #2018 and #2029.

### Read snippet
```js
const show = (u, r) => r.text().then(t => console.log(u, t.slice(0, 1500)));
fetch('/api/v1/radar', {credentials:'include'}).then(r=>r.json()).then(j=>console.log('degraded', JSON.stringify(j.degraded_sources)));
fetch('/api/v1/standup/today', {credentials:'include'}).then(r=>show('today', r));
for (const f of ['slack','markdown']) fetch('/api/v1/standup/generate', {method:'POST', credentials:'include', headers:{'Content-Type':'application/json'}, body: JSON.stringify({format:f})}).then(r=>show(f,r));
```

### Console fallback for reconnecting
```js
fetch('/api/v1/settings/integrations/github/disconnect', {method:'POST', credentials:'include'}).then(r=>r.json()).then(d=>{console.log('disconnect',d); return fetch('/api/v1/settings/integrations/github/connect',{credentials:'include'});}).then(r=>r.json()).then(d=>{console.log('connect',d); if(d.auth_url) location.href=d.auth_url;});
```
