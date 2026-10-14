"""Build the Zotero plugin package dist/zotero-easyread-<version>.xpi from zotero/ and LICENSE."""
from pathlib import Path
import hashlib, json, zipfile

root=Path(__file__).resolve().parent
dist=root/'dist';dist.mkdir(exist_ok=True)
version=json.loads((root/'zotero/manifest.json').read_text(encoding='utf-8'))['version']
xpi=dist/f'zotero-easyread-{version}.xpi'
with zipfile.ZipFile(xpi,'w',zipfile.ZIP_DEFLATED) as z:
    for p in sorted((root/'zotero').rglob('*')):
        if p.is_file():z.write(p,p.relative_to(root/'zotero').as_posix())
    z.write(root/'LICENSE','LICENSE')
print(xpi.relative_to(root).as_posix(),hashlib.sha256(xpi.read_bytes()).hexdigest())
