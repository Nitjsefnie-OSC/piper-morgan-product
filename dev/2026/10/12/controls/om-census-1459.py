import collections
import re
import subprocess

files = subprocess.check_output(
    ["git", "grep", "-lE", 'original_message|context\\.get\\("message"', "--", "services", "web"],
    text=True,
).split()
A = re.compile(r'context(?:\s*or\s*\{\})?\s*\.get\(\s*["\']original_message["\']')
Cidx = re.compile(r'context\s*\[\s*["\']original_message["\']\s*\]')
ATTR = re.compile(r"\b(\w+)\.original_message\b(?!\s*=[^=])")
SETATTR = re.compile(r"\b(\w+)\.original_message\s*=[^=]")
SETDICT = re.compile(r'context\s*\[\s*["\']original_message["\']\s*\]\s*=[^=]')
KW = re.compile(r"\boriginal_message\s*=\s*")  # kwarg at construction
DK = re.compile(r'["\']original_message["\']\s*:')  # dict literal key
MSGFB = re.compile(r'context\.get\(\s*["\']message["\']')
rows = collections.Counter()
detail = collections.defaultdict(list)
for f in files:
    for i, l in enumerate(open(f), 1):
        s = l.strip()
        if s.startswith("#"):
            continue
        if SETDICT.search(l):
            rows["set:dict-index"] += 1
            detail["set:dict-index"].append(f"{f}:{i}")
            continue
        if SETATTR.search(l):
            rows["set:attr"] += 1
            detail["set:attr"].append(f"{f}:{i}")
            continue
        if DK.search(l):
            rows["set:dict-literal-key"] += 1
            detail["set:dict-literal-key"].append(f"{f}:{i}")
            continue
        if KW.search(l) and "def " not in l:
            rows["set:kwarg"] += 1
            detail["set:kwarg"].append(f"{f}:{i}")
            continue
        attr = ATTR.search(l)
        dict_ = A.search(l) or Cidx.search(l)
        if attr and dict_:
            rows["read:B attr-or-dict"] += 1
            detail["read:B attr-or-dict"].append(f"{f}:{i}")
        elif attr:
            rows["read:attr-only"] += 1
            detail["read:attr-only"].append(f"{f}:{i}")
        elif A.search(l):
            rows["read:A dict-get"] += 1
            detail["read:A dict-get"].append(f"{f}:{i}")
        elif Cidx.search(l):
            rows["read:C dict-index"] += 1
            detail["read:C dict-index"].append(f"{f}:{i}")
        elif MSGFB.search(l):
            rows["read:message-fallback"] += 1
            detail["read:message-fallback"].append(f"{f}:{i}")
for k, v in sorted(rows.items()):
    print(f"{v:4} {k}")
print()
for k in sorted(detail):
    print("==", k)
    for d in detail[k]:
        print("  ", d)
