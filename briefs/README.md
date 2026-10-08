# SecOps 每周简报

每周一 **07:30 (UTC+8)** 发布，每期深度介绍不超过 **5** 个 startup / technology。

## 文件命名

```
briefs/YYYY-MM-DD-secops-landscape.md           # 完整周报
briefs/YYYY-MM-DD-secops-landscape-outline.md   # 自动生成大纲（可选）
```

日期用当周简报发布日（周一）。

## 本地生成大纲

```powershell
.venv\Scripts\activate
python scripts/discover.py
python scripts/generate_brief.py --write
```

完整简报由 Agent 基于 registry 未发布候选、近期报告与 tier A/B 来源撰写。

## Cursor Automation

定时：**每周一 07:30**。Agent 应：

1. 在仓库根目录运行 discovery（`python scripts/discover.py`），再生成大纲（`python scripts/generate_brief.py --write`）。
2. 阅读大纲、`topics/registry.yaml` 未发布高分候选，以及 `reports/INDEX.md` 已发布报告，避免重复选题。
3. 撰写中文周报，深度介绍不超过 5 项，保存为 `briefs/YYYY-MM-DD-secops-landscape.md`。
4. Commit 并 push 到 `main`。
