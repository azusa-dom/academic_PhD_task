#!/usr/bin/env python3
from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parent.parent
errors=[];checked=0
for line in (root/'SHA256SUMS.txt').read_text().splitlines():
 if not line.strip():continue
 expected,name=line.split('  ',1);p=Path(name)
 if p.is_absolute() or '..' in p.parts:errors.append('unsafe path');continue
 file=root/p
 if not file.is_file() or file.is_symlink() or hashlib.sha256(file.read_bytes()).hexdigest()!=expected:errors.append(name)
 checked+=1
print(json.dumps({'checked_files':checked,'passed':not errors,'errors':errors},ensure_ascii=False,indent=2))
raise SystemExit(1 if errors else 0)
