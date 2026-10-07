# 来源与本仓库改动

本仓库收录 [AICrossSim/PLENA](https://github.com/AICrossSim/PLENA) 的公开 RTL 与提供的 RTL-v6 研究快照。PLENA 基础框架与第三方模块保留文件中的版权声明。面向 Qwen3 的数据通路优化及项目成绩见 [README](README.md)；2026-10-04 的仓库整理另增加 45 处中文注释、独立运行脚本和本机验证。

所有 PLENA 核心依赖已直接纳入普通 Git 文件。导入的 `.gitmodules` 存在 `docs/provenance/gitmodules/` 中作为来源记录；不参与 checkout。第三方 Python/Rust 包仍由原有依赖清单安装。模型权重、环境、构建缓存、原始压缩包不入 Git。

源码清单：[逐文件原始/当前 SHA256 与 commit](docs/provenance/source-manifest.json)；[注释清单](docs/provenance/annotations.json)。两套工程共 1,434 个导入文件；45 处新增注释之外的源码字节与导入版本一致。上游 README、配置、脚本和版权头保留原内容；本仓库的运行入口位于 `scripts/`。

RTL 归档：`03_PLENA_RTL_source_20260924.tar.zst`，SHA256 `979103A40F877590A4A8213F35DA4E3269CB889BF3E10E850BF5ED2B57026CC8`。打包名含 9 月 24 日；其 HEAD `1e0eb060` 的提交日期为 8 月 22 日。源码从 tracked commit 导出；原包两份 dirty Synopsys debug 脚本及旧 build 保留在本地原工作区。

历史记录与独立仓库复测按目录保存，见[日志索引](evidence/README.md)。原始文件保留日期和 manifest；2026-10-04 独立仓库验证的配置及结果见 [VALIDATION](docs/VALIDATION.md)。

本仓库从上述快照和公开基线创建，两套工程保留各自的 Compiler/Tools；具体版本见[配套表](docs/COMPATIBILITY.md)。原 `RTLFile` 本地工作区保留作归档核对。

## 版权与引用

保留各源码文件版权头和组件中已有 LICENSE。公开 RTL 基线采用 [Apache-2.0](reference/upstream-release/LICENSE)，其 [第三方声明](reference/upstream-release/THIRD_PARTY_LICENSES.md)列出 lowRISC/OpenTitan primitives 与 Gary Guo 的 TileLink 库。DesignWare 实现未随仓提供，对应综合路径需要自行配置工具与库。研究快照按自身已有声明处理，未另行补写统一授权。

2026-10-07 文档整理：精简首页，补充核心源码链接与日志索引；删除未被运行入口引用的 `requirements-cpu.txt`，统一指向 `requirements-rtl.txt`；修正本页误带的软件仓库 OSWorld/ASAP7 说明。源码、依赖版本、版权和历史日志未改动。

原论文：[Combating the Memory Walls: Optimization Pathways for Long-Context Agentic LLM Inference](https://arxiv.org/abs/2509.09505)。需要学术引用时使用对应上游 README 的 BibTeX。
