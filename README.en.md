# Zotero → EasyRead

[简体中文](README.md) · [EasyRead](https://github.com/Edwardxlai/easyread)

Manage papers in Zotero, read them in EasyRead, and manually copy reading notes back into a managed Zotero child note.

This repository is based on [apple5089/zotero-easyread](https://github.com/apple5089/zotero-easyread) and adds macOS support and a Zotero settings pane. It is an independent community integration. Thanks to [@Edwardxlai](https://github.com/Edwardxlai) for EasyRead and [@apple5089](https://github.com/apple5089) for the original plugin. This project is not officially maintained or endorsed by EasyRead.

## Features

- Right-click a Zotero item or PDF to read it in EasyRead. Full SHA-256 deduplication reuses an existing paper.
- Send up to 20 papers at once without automatically translating them.
- Copy paper notes, highlights, comments, questions, original PDF page numbers, English paragraph context, and saved sidebar AI answers into a child note.
- Reuse unchanged notes. Preserve manually edited Zotero notes and create a new managed version on the next sync.
- Reopen the corresponding paper and paragraph through saved links, using EasyRead 1.3.1+'s official `easyread://open` desktop entry.
- Discover EasyRead's local service port automatically.

Sync is **manual and one-way, EasyRead → Zotero**. It does not create native Zotero PDF annotations, merge arbitrary edits in both applications, or copy full AI chat histories. Translation and questions use the models and costs configured in EasyRead.

## Building the XPI

The XPI is the Zotero plugin package. Download it from [Releases](https://github.com/gulubao/zotero-easyread/releases), or build it from source with only the Python 3 standard library:

```bash
git clone https://github.com/gulubao/zotero-easyread.git
cd zotero-easyread
python3 build.py
```

On Windows use `py` instead of `python3`. The script writes `dist/zotero-easyread-<version>.xpi` and prints its SHA-256. The XPI contains everything under `zotero/` (`manifest.json`, `bootstrap.js`, `bridge.js`, `core.js`, `prefs.js`, `prefs.xhtml`) plus `LICENSE`. `dist/` is not tracked by Git.

`<version>` comes from `version` in `zotero/manifest.json`. After changing code, run `python3 build.py` again and reinstall with step 2 below. Bumping `version` in both `zotero/manifest.json` and `zotero/bridge.js` makes it easy to see which build Zotero has loaded. The plugin ID stays the same, so a new build replaces the old one and keeps its links and settings.

## Installation

Real integration tests cover **macOS, Zotero 10.0.6, and EasyRead 1.4.2**; the original plugin was tested on **Windows, Zotero 10.0.5-beta.2, and EasyRead 1.3.0 / 1.3.2**. Other Zotero 8–10 versions and Linux are untested.

1. Download `zotero-easyread-<version>.xpi` from Releases, or build it as described above.
2. In Zotero, open Tools → Plugins → gear menu → Install Plugin From File and choose that XPI.
3. Start EasyRead. Default locations need no setup: `/Applications/EasyRead.app` on macOS, `C:\Program Files\EasyRead\EasyRead.exe` on Windows. Otherwise set the path in **Zotero Settings → EasyRead** (also opened by Tools → `EasyRead：连接设置…`); blank means auto-detect. Discovery checks the configured data directory, `<installation>/data` on Windows, then `~/EasyRead`. Menu labels are currently Chinese.
4. Right-click an item/PDF → Zotero → EasyRead → `用 EasyRead 阅读`.
5. After reading, choose `同步 EasyRead 阅读笔记` on the same item.

On macOS the plugin opens the desktop app with `open -a EasyRead.app easyread://open?...`; if the app is not at the configured path it hands the link to whichever app registered `easyread://`, and only then falls back to the local reader page in a browser.

The first single-paper import requests translation by default; this can be disabled in settings. Batch import never starts translation automatically.

PDFs must be downloaded locally and at most 200 MB. A regular item uses its preferred PDF; selecting an attachment explicitly chooses that PDF. Standalone PDFs need a parent item before note sync. Read-only libraries cannot receive notes.

## Data and compatibility

Association state is stored in the Zotero profile (`zotero-easyread.json`), startup state in `zotero-easyread-status.json`. Do not publish runtime data or model credentials.

The plugin uses the API v1, PDF fingerprint, and reading data schema documented by [EasyRead](https://github.com/Edwardxlai/easyread/blob/main/docs/api.md), plus Zotero's MenuManager and settings pane APIs. Replacing a PDF's content links the new version and keeps notes from the old one; an unknown API version asks you to update the plugin. The plugin does not auto-update; download new versions from Releases and reinstall.

## License

[MIT](LICENSE).
