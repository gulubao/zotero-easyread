# Changelog

## 0.2.0 — 2026-10-14

- macOS support: default to `/Applications/EasyRead.app` and `~/EasyRead`, start or focus the app and deliver `easyread://open` links through `/usr/bin/open -a` (an `.app` bundle cannot be passed to `exec`), fall back to the system `easyread://` handler, then to the local reader page.
- Settings moved to a regular Zotero settings pane (Zotero Settings → EasyRead); the Tools menu entry opens it. Blank paths mean auto-detect, defaults come from `prefs.js`.
- Removed the hard-coded `D:\Program Files\EasyRead\EasyRead.exe` fallback when EasyRead is not running.
- Update URL points to this fork so upstream releases do not replace it.
- Verified on macOS with Zotero 10.0.6 and EasyRead 1.4.2: 26 native harness checks (including settings pane open/visible/save) and a real `easyread://` jump to a paragraph.

## 0.1.1 — 2026-10-05

- Discover EasyRead's migrated Windows `<installation>/data` directory automatically while preserving explicitly configured live custom directories.
- Negotiate the documented API v1 and use native `easyread://open` desktop links on EasyRead 1.3.1+, avoiding archive patches for supported releases.
- Read notes through documented `part/paper`, `part/reader`, and `part/discussion` endpoints instead of the side-effecting reader `state` endpoint.
- Provide an update URL in the plugin manifest and isolate test-profile application update settings.
- Verified 18 real application checks against EasyRead 1.3.2 and Zotero 10.0.5-beta.2, plus new compatibility tests.

## 0.1.0 — 2026-10-03

- Initial public release: Zotero context-menu import/open, PDF fingerprint deduplication, manual one-way reading note sync, edited-note preservation, and saved paragraph links.
- Optional reversible Windows Electron desktop bridge.
- Generalized installation instructions, English/Chinese documentation, synthetic archive fixtures and cross-platform core CI.
- Real application integration verified on Windows with Zotero 10.0.5-beta.2 and EasyRead 1.3.0.
