# S5: GitHub reads with the Alpha app revoked (#1965, #1889, plus #2012's Test)

**Owner**: PA, run by xian. **Written** 2026-10-15 09:48 from the code on main (Lead's landing `4a39c01ce2`).
**Run it only after the promotion that carries it**: alpha `/health` `git_sha` must not be `5e5f3366c4`. PA
confirms the sha has the fix before you start. About 10 minutes.

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
2. Settings → Integration Health → GitHub → **Test**. **Pass**: it fails, and says to reconnect. (On 10-14 it
   said "connection successful".) CXO judges the wording.

## 4. Reconnect
Integrations → GitHub → **Disconnect** → confirm, then **Connect with GitHub** (#2017's fix rides the same
promotion). If Disconnect still does nothing, use the console fallback below and tell PA.

## 5. After
Run the read snippet once more. **Pass**: `degraded []` and your issues are back.

Paste each console output to PA (or into the PA chat). PA relays the readings to Lead and CXO and comments on
#1965, #1889 and #2012.

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
