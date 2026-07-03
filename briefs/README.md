# SecOps 每日简报

工作日 **07:30 (UTC+8)** 发布，每期深度介绍不超过 **5** 个 startup / technology。

## 文件命名

```
briefs/YYYY-MM-DD-secops-landscape.md      # 完整简报
briefs/YYYY-MM-DD-secops-landscape-outline.md  # 自动生成大纲（可选）
```

## 本地生成大纲

```powershell
.venv\Scripts\activate
python scripts/generate_brief.py --write
```

完整简报由 Agent 基于 registry 未发布候选、近期报告与 tier A/B 来源撰写。

## 自动化

- **GitHub Actions:** [`.github/workflows/daily-brief.yml`](../.github/workflows/daily-brief.yml) 每日 UTC 23:30（= 北京时间次日 07:30）生成大纲并开 PR。
- **Cursor Automation（推荐）：** 定时触发 Agent，提示词示例：

  > 阅读 `briefs/` 最新大纲与 `topics/registry.yaml` 前 5 名未发布候选，撰写今日 SecOps landscape 简报（中文，不超过 5 项深度介绍），保存为 `briefs/YYYY-MM-DD-secops-landscape.md` 并 commit push。
