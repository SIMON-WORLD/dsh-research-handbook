# Contributing

欢迎贡献！无论是修正错误、补充实测、新增章节还是改进排版。

## 如何贡献

1. **先看现有章节**：避免重复内容。想写的新主题先开 Issue 讨论定位。
2. **Fork + PR**：分支命名 `docs/<topic>` 或 `fix/<topic>`。
3. **实测优先**：每个命令必须在你自己的环境跑过，并在文中注明：

   ```text
   - 验证环境：Windows 11 / dsh 0.1.1-rc.2 / Node.js 24.x
   - 验证日期：2026-08-26
   ```

4. **中文为主**：术语保留英文原文（如 profile / bundle / headless）。

## 结构约定

- `docs/NN-topic.md`：章节文件，编号两位。
- `docs/cheatsheet.md`：一页速查卡，保持精简。
- `scripts/`：可运行的示例脚本（验证过的才放这里）。
- `release-kit/`：公众号 / 小红书 / 知乎 / 短视频发布物料。

## 提交信息

建议使用 Conventional Commits：

```
docs: 新增 Windows 排坑章节
fix: 修正速查卡中推理档位说明
```

## 行为准则

友善、尊重、对事不对人。违反者可被移除贡献资格。
