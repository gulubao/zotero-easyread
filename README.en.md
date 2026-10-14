# Zotero → EasyRead

[简体中文](README.md) · [EasyRead](https://github.com/Edwardxlai/easyread)

Manage papers in Zotero, read them in EasyRead, and manually copy reading notes back into a managed Zotero child note.

This is an independent community integration. Thanks to [@Edwardxlai](https://github.com/Edwardxlai) for EasyRead. This project is not officially maintained or endorsed by EasyRead.

## Features

- Right-click a Zotero item or PDF to read it in EasyRead. Full SHA-256 deduplication reuses an existing paper.
- Send up to 20 papers at once without automatically translating them.
- Copy paper notes, highlights, comments, questions, original PDF page numbers, English paragraph context, and saved sidebar AI answers into a child note.
- Reuse unchanged notes. Preserve manually edited Zotero notes and create a new managed version on the next sync.
- Reopen the corresponding paper and paragraph through saved links with the optional desktop bridge.
- Discover EasyRead's local service port automatically.

Sync is **manual and one-way, EasyRead → Zotero**. It does not create native Zotero PDF annotations, merge arbitrary edits in both applications, or copy full AI chat histories. Translation and questions use the models and costs configured in EasyRead.

## Installation

Real integration tests cover **Windows, Zotero 10.0.5-beta.2, and EasyRead 1.3.0 / 1.3.2**, and **macOS, Zotero 10.0.6, and EasyRead 1.4.2**. Other Zotero 8–10 versions and Linux are unverified.

1. Build `dist/zotero-easyread-<version>.xpi` with `python3 build.py` (or download it from Releases).
2. In Zotero, open Tools → Plugins → gear menu → Install Plugin From File.
3. Start EasyRead. Default locations need no setup: `/Applications/EasyRead.app` on macOS, `C:\Program Files\EasyRead\EasyRead.exe` on Windows. Otherwise set the path in **Zotero Settings → EasyRead** (also opened by Tools → `EasyRead：连接设置…`); blank means auto-detect. Discovery checks the configured data directory, `<installation>/data` on Windows, then `~/EasyRead`. Menu labels are currently Chinese.
4. Right-click an item/PDF → Zotero → EasyRead → `用 EasyRead 阅读`.
5. After reading, choose `同步 EasyRead 阅读笔记` on the same item.

On macOS the plugin opens the desktop app with `open -a EasyRead.app easyread://open?...`; if the app is not at the configured path it hands the link to whichever app registered `easyread://`, and only then falls back to the local reader page in a browser.

The first single-paper import requests translation by default; this can be disabled in settings. Batch import never starts translation automatically. EasyRead 1.3.1+ opens through its official desktop protocol, without an archive patch. Older unpatched releases open in a local browser.

PDFs must be downloaded locally and at most 200 MB. A regular item uses its preferred PDF; selecting an attachment explicitly chooses that PDF. Standalone PDFs need a parent item before note sync. Read-only libraries cannot receive notes.

## Optional desktop bridge for EasyRead 1.3.0 only

EasyRead 1.3.1+ uses official `easyread://open` links and needs no desktop patch. See [EasyRead's API contract](https://github.com/Edwardxlai/easyread/blob/main/docs/api.md).

Requires Python 3.10+ and PowerShell 7+. Close EasyRead normally, then run from the source or release ZIP:

```powershell
python desktop/patch_asar.py --source "C:\Program Files\EasyRead\resources\app.asar"
pwsh -File install.ps1 -EasyReadDir "C:\Program Files\EasyRead"
```

Use your actual installation path. Run the desktop installer as administrator if required by Windows permissions. It verifies the archive structure and hashes, backs up the original archive, and installs only the desktop bridge. It does not alter Zotero versions, update settings, or other plugins.

EasyRead upgrades may replace this patch; browser reading remains available. To restore the desktop archive, close EasyRead normally and run `pwsh -File restore.ps1`. Uninstall the Zotero plugin separately through its plugin manager. Reading data and notes are retained.

## Development

Node.js 22+ and Python 3.10+, with no third-party npm/pip dependencies:

```bash
node --test tests/core.test.cjs tests/compat.test.cjs
python -m unittest discover -s tests -p "test_*.py" -v
python build.py
```

The build produces an XPI and an integration-source ZIP; it does not redistribute EasyRead. CI runs core tests on Windows, macOS, and Linux, while real application integration has only been tested on Windows. See [VALIDATION.md](VALIDATION.md).

Association state is stored in the Zotero profile (`zotero-easyread.json`). Desktop requests are stored in `zotero-bridge/` inside the EasyRead data directory. Do not publish runtime data or model credentials. This integration depends on EasyRead's local APIs, reading data schema, and Electron layout, which may change.

## License

MIT for this integration. See [third-party notices](THIRD_PARTY_NOTICES.md) for upstream attribution and [CONTRIBUTING.md](CONTRIBUTING.md) to contribute.
