# Zotero → EasyRead

[English](README.en.md) · [EasyRead 原项目](https://github.com/Edwardxlai/easyread)

在 Zotero 管理论文，用 EasyRead 阅读。右键发送 PDF，复用已有译文和阅读记录，再把阅读笔记手动同步回 Zotero。

本仓库基于 [apple5089/zotero-easyread](https://github.com/apple5089/zotero-easyread) 修改，增加了 macOS、Ubuntu 支持和 Zotero 设置页。这是独立的社区集成项目。感谢 [@Edwardxlai](https://github.com/Edwardxlai) 开发 EasyRead、[@apple5089](https://github.com/apple5089) 开发原插件；本项目未获得 EasyRead 官方维护或背书。

## 功能

- 右键“用 EasyRead 阅读”：首次导入；同一 PDF 按完整 SHA-256 去重。
- 多选“发送到 EasyRead（批量，先不翻译）”：每批最多 20 篇。
- 右键“同步 EasyRead 阅读笔记”：整篇心得、划线、批注、问题、原 PDF 页序号、段落英文和保存到页边的 AI 回答，写入文献的专属子笔记。
- 同步内容不变时复用笔记。在 Zotero 手动编辑专属笔记后，保留该版本并创建新的受管理版本。
- “返回 EasyRead”链接可打开同一 PDF，并通过 EasyRead 1.3.1+ 的官方 `easyread://open` 入口在桌面版定位段落。
- 自动发现本机服务端口，无需固定端口或云端中转。

同步是 **手动、单向 EasyRead → Zotero**。不创建 Zotero PDF 原文高亮，不合并两边任意修改，不同步完整 AI 聊天记录。翻译与问答沿用 EasyRead 中配置的模型及其费用规则。

## 生成 XPI

XPI 就是 Zotero 插件的安装包。可以直接从 [Releases](https://github.com/gulubao/zotero-easyread/releases) 下载，也可以从源码生成：只用 Python 3 标准库，不用装任何依赖。

```bash
git clone https://github.com/gulubao/zotero-easyread.git
cd zotero-easyread
python3 build.py
```

Windows 上把 `python3` 换成 `py`。运行后生成 `dist/zotero-easyread-<版本>.xpi` 并打印它的 SHA-256。XPI 里是 `zotero/` 目录下的全部文件（`manifest.json`、`bootstrap.js`、`bridge.js`、`core.js`、`prefs.js`、`prefs.xhtml`）加上 `LICENSE`。`dist/` 不进 Git。

`<版本>` 取自 `zotero/manifest.json` 的 `version`。改了代码要重新运行 `python3 build.py`，再按下面第 2 步重新安装；建议同时提高 `zotero/manifest.json` 和 `zotero/bridge.js` 里的 `version`，便于在 Zotero 插件列表里分辨装的是哪一版。插件 ID 不变，新版会直接替换旧版，关联记录和设置都保留。

## 安装

已做真实软件测试的环境为 **macOS、Zotero 10.0.6、EasyRead 1.4.2**；原插件在 **Windows、Zotero 10.0.5-beta.2、EasyRead 1.3.0 与 1.3.2** 上测试过。Ubuntu 按 EasyRead 官方 AppImage 与 `~/EasyRead` 数据目录接入，尚未做同样的联调。清单允许 Zotero 8 到 11；除此之外不能保证兼容。

1. 从 Releases 下载 `zotero-easyread-<版本>.xpi`，或按上一节自己生成。
2. Zotero → 工具 → 插件 → 齿轮菜单 → 从文件安装插件，选择这个 XPI。
3. 启动 EasyRead。默认安装位置无需设置：macOS 为 `/Applications/EasyRead.app`，Windows 为 `C:\Program Files\EasyRead\EasyRead.exe`。Ubuntu 留空时优先使用已注册的 EasyRead `.desktop` 启动项，否则查找 `EasyRead*.AppImage`（`~/Applications`、`~/AppImages`、`~/.local/bin`、`/opt`、`/usr/local/bin`、下载目录和桌面），最后才用 PATH 上的 `easyread`。装在别处时到 **Zotero 设置 → EasyRead**（也可从“工具 → EasyRead：连接设置…”进入）填写路径，留空即自动检测。数据目录依次为：已设置的目录、Windows 安装目录下的 `data`、用户目录下的 `EasyRead`（macOS 与 Ubuntu 的默认位置）。
4. 右键文献或已下载的 PDF 附件 → **Zotero → EasyRead** 子菜单 → 用 EasyRead 阅读。
5. 阅读后在同一条目上执行“同步 EasyRead 阅读笔记”。

macOS 上插件通过 `open -a EasyRead.app easyread://open?...` 打开桌面版并定位段落。Ubuntu 上运行找到的程序并传入同一个 `easyread://` 链接；直接打开 AppImage 时，若系统禁止非特权用户命名空间，会附上 `--no-sandbox`。找不到程序或程序无法启动时，用 `xdg-open` 交给系统已注册的处理程序。都失败才用浏览器打开本机阅读页。AppImage 需要可执行权限（`chmod +x`）。

首次单篇导入默认请求翻译，可在设置中关闭。批量发送始终不自动翻译。

PDF 必须已下载到本机，最大 200 MB。文献包含多个 PDF 时默认使用 Zotero 首选 PDF，也可明确选中某个附件。独立 PDF 需关联文献后才能回写子笔记；只读文献库无法回写。

## 数据与兼容

关联记录保存在 Zotero 配置目录的 `zotero-easyread.json`；启动状态在 `zotero-easyread-status.json`。请勿公开这些运行数据或模型配置。

当前使用 [EasyRead 文档](https://github.com/Edwardxlai/easyread/blob/main/docs/api.md)中的 API v1、PDF 指纹和阅读数据结构，以及 Zotero MenuManager 与设置页接口。PDF 内容替换后会关联新版本，保留旧版本笔记；未知 API 版本会明确提示更新插件。Zotero 10 及以上要求清单里有 `update_url`，否则安装会被拒绝，并显示“可能无法与该版本的 Zotero 兼容”。该地址指向 Releases 上的 `update.json`，目前没有发布这个文件，所以不会自动升级；新版本请到 Releases 下载后重新安装。

## 许可证

[MIT](LICENSE)。
