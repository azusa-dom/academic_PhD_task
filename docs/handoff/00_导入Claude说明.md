# 导入 Claude

这个包包含科研背景、当前工作流、工具与环境说明、持续协作规则，以及 24 个选定 skills 的本地副本。它是个人交接材料，不含科研数据、认证信息、虚拟环境或稿件全文，也没有替你安装软件或改变 Claude 设置。

## Claude 网页或桌面聊天

创建或打开科研 Project，将 `01_我的科研工作流与当前状态.md`、`02_Skills与工具清单.md` 和 `03_软件包与计算环境.md` 上传到项目知识库，把 `CLAUDE.md` 的正文复制到项目 instructions，然后发送下面的接续提示。普通聊天也可以上传这三个 Markdown，但持续项目优先使用 Project。项目知识文件和项目 instructions 的操作依据为 [Claude 官方项目说明](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)，2026-10-09 核查。

请先解压后选择文件，不要假定整个交接 ZIP 会自动变成已安装 skills。文件里列出的本机和 CSF3 路径是定位信息，网页版 Claude 无法仅凭路径读取相应文件。具体稿件任务仍需上传当前版本和必要证据文件。

## Claude Code

在你选定的科研项目里保留这三个说明文档，把本包 `CLAUDE.md` 合并进项目既有规则文件；已有规则时不要直接覆盖。官方说明支持项目根目录的 `CLAUDE.md`，见 [Claude Code 项目记忆](https://code.claude.com/docs/en/memory)。

根据任务选择 `skills/` 下的目录，将完整目录放入项目 `.claude/skills/<skill-name>/`，或本人机器 `~/.claude/skills/<skill-name>/`；每个目录应保留 `SKILL.md` 与它的 references/scripts/assets。相同名称已存在时先比较版本，不覆盖已用版本。位置和 `SKILL.md` 格式依据为 [Claude Code skills 官方文档](https://code.claude.com/docs/en/skills)，2026-10-09 核查。只复制所需的 skills 即可。

在同一台 Mac 上也可向 Claude Code 提供原目录读取授权；若在其他机器运行，本包 provenance 中的旧路径仅用于追溯。当前包不含 MCP 服务、浏览器会话、API 凭证或远端登录配置，不能据此假定这些能力已接入。

## 第一条接续提示

> 请先阅读我上传的科研工作流、skills 清单、软件环境说明，并遵循协作规则。我的当前主线是 cine-CMR 批判性叙述综述和区域运动/应变的探索性研究，最终博士问题仍未确定。先用连续中文段落复述你理解的研究主线、当前交付状态和关键验证边界，再根据我接下来指定的任务选择必要的 skills。不要从头重做已有检索，不要把 AI 内部检查当作者批准，也不要把探索性输出写成准确性或临床验证。如果需要实际执行，请先核对你能读取的源码、实际工具和数据授权；缺少能力时如实说明。

## 文件与来源

`evidence/` 保存本次用于判定状态的简短项目记录，包括 v9 执行日志与状态、DENSE 环境/QC、图件与软件分支的报告。它们是原记录副本，本次未重新验证原报告中的全部检查。

`PROVENANCE.json` 记录每个 skill 的源路径、源文件和复制哈希；`MANIFEST.sha256` 记录本包文件身份。目录内容不等于软件安装或科研质量认证。
