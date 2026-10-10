# 月影书屋 v1.0

二次元塔罗占卜桌面程序：每日一签 + 主题占卜 + 78 张牌图鉴。单文件、零依赖、可整目录删除。

## 下载

- **一键包（推荐）**：[yueying-shuwu-v1.0.zip](https://github.com/Shione0721/yueying-shuwu/releases/latest/download/yueying-shuwu-v1.0.zip) —— 解压到任意固定文件夹，双击 `月影书屋.exe` 即可使用。

## 功能

- **每日一签**：每天抽一张牌，跨启动记住，第二天自动换新
- **主题占卜**：爱情 / 事业 / 学业 / 财运 / 人际 / 健康 / 综合，七选一
- **8 种牌阵**：单张牌 / 时间之流 / 圣三角 / 身心灵 / 处境·行动·结果 / 二选一 / 六芒星 / 凯尔特十字
- **模式切换**：22 张大阿卡纳 ⇄ 78 张标准塔罗，一键切换
- **图鉴全览**：78 张牌，含寓意与正 / 逆位解读

## 使用

1. 双击 `月影书屋.exe`（首次启动稍慢，请稍等窗口出现）
2. 顶部按钮切换 22 / 78 张模式
3. 「抽一张」看今日签，或选方面 + 牌阵后点「开始占卜」

## 卡面版权

卡面图片来自《Mystical Manga Tarot》塔罗牌组（elvitarot.com），版权归原作者所有，仅供个人学习与展示。

## 环境要求

- Windows 10 / 11，需已安装 Microsoft Edge WebView2 Runtime（Windows 11 自带）

## 开发

- 源码在 `src/`：`tarot.py`（pywebview 桌面入口）+ `tarot.html`（界面与牌义）+ `cards/`（78 张卡面）
- 打包命令（在 `src/` 下执行）：

```bash
python -m PyInstaller --onefile --windowed --clean --noconfirm --name TarotDivine --icon icon.ico --add-data "tarot.html;." --add-data "cards;cards" tarot.py
```

## License

MIT © Shione0721
