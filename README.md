# Academic Writing Skills

面向 AI 领域科研写作的技能，重点解决：文献依据不清、技术解释难懂、方法堆砌、段落缺少因果、总结重复，以及带有AI套话的表述。

## 已收录

| 技能 | 用途 | 主要交付 |
| --- | --- | --- |
| [deepresearch](skills/deepresearch/SKILL.md) | 从关键词梳理研究问题、设计章节、核验论文并综合进展 | 章节大纲及带摘要、原文位置的文献包 |
| [write-paper](skills/write-paper/SKILL.md) | 组织原创论文文献库与引用计划，自动选择六章段落模板 | 不少于40篇入选文献的引用分配、正文及章节或全篇核查结果 |
| [write-review](skills/write-review/SKILL.md) | 根据段落或小节大纲及文献证据撰写综述 | 有核心论点、机制解释、证据边界及必要缺口说明的正文 |
| [paperwrite](skills/paperwrite/SKILL.md) | 依据大纲和证据撰写科研正文 | 讲清问题、设计原因、方法联系与适用边界的段落 |
| [rewrite](skills/rewrite/SKILL.md) | 改写难懂段落、补清逻辑、去除AI套话 | 保留事实与结论强度的改稿及必要检查记录 |

`cite`（基于文献库匹配引用）和 `review`（投稿前检查）仍在计划中，本仓库没有将它们包装为已完成技能。

## 安装

把需要的技能目录放到目标项目的 `.agents/skills/`，保持目录名。`write-paper` 与 `write-review` 可独立安装；与 `deepresearch` 配合时复用已有调研和文献包。`write-paper` 自带文献流程与六章模板，按当前任务只读取相关模板。`paperwrite` 使用 `deepresearch` 与 `rewrite` 的参考文件，使用它时应将这三个目录并列安装。

在这个仓库的根目录执行以下命令，可安装到一个新目录；目标已存在时先检查差异，避免覆盖本地修改：

```bash
mkdir -p /path/to/your-project/.agents/skills
cp -R skills/deepresearch skills/write-paper skills/write-review skills/paperwrite skills/rewrite /path/to/your-project/.agents/skills/
```

也可整组安装到用户级 `~/.codex/skills/`。安装后开启新的会话，确认所安装的技能被发现。搜索、论文读取、TeX编译等能力由实际使用环境提供，仓库不附带这些工具或任何账号凭据。

## 使用

- 调研：`使用 $deepresearch，研究关键词是……，先给出范围和章节安排供我确认。`
- 原创论文：`使用 $write-paper，复用或建立文献库与逐篇引用计划，识别当前章节并按相应模板撰写指定段落。`
- 综述写作：`使用 $write-review，根据现有段落大纲和文献包提炼核心论点，撰写……段落或小节。`
- 原有写作流程：`使用 $paperwrite，根据现有章节大纲和文献包撰写……小节。`
- 改写：`使用 $rewrite，解释并修复下面段落的理解断点，不改变事实和结论强度。`

普通交互式小修改可以直接按反馈处理，不必每次运行完整技能流程。大纲确认、单语/双语、输出文件和是否只在对话中测试，均沿用用户本轮要求及项目已有决定。

## 写作约束

- 按共同问题组织方法，解释关键设计为何有用，不按年份逐篇堆砌。
- 摘要支持贡献概述；机制须查方法，效果与局限须查相应实验或讨论。
- 组织计划留在底稿，不直接写成论文正文；总结回答已解决程度与具体剩余困难。
- 改写保留事实、引用及证据强度；脚本通过不代表科学内容或可读性已经获认可。

`deepresearch` 保留了我们明确选择的筛选条件：指定主会、期刊JIF大于10、单篇引用超过5000，满足一项即可。这是本技能的选材约定，不应当作研究质量的普遍判定标准。

`write-paper` 的全文流程要求至少40篇入选文献，每篇预分配到具体段落及主张，并在最终正文中实际引用。单章任务只核对本章计划引用的落实情况，整篇完成时检查全部入选文献；不要求每章引用全部文献。

## 检查脚本

改写记录检查器仅依赖Python标准库：

```bash
python3 skills/rewrite/scripts/check_review.py /path/to/run/review.json
```

它核对最终稿哈希、引用片段和记录字段，不判断文献是否真实、机制是否正确或段落是否易懂。

## 来源与适配

初版三个技能来自综述写作中协作开发的独立草案。随后加入 `write-review` 与 `write-paper`，分别支持综述和原创论文写作，并完善 `deepresearch` 的逐篇记录要求；`paperwrite` 保留供原有流程使用。仓库不附带原项目的论文正文、PDF、参考文献库或私人配置。选材标准与本轮适配范围详见[适配说明](docs/portability.md)。

现有技能头部声明的许可为 **CC-BY-NC-SA-4.0**，本次整理保留该声明，参见[许可说明](LICENSE.md)。
