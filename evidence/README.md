# 日志与结果

本目录保存已同步到仓库的日志。另一台计算机上的项目最终成绩及材料同步情况见 [软件项目结果](https://github.com/Sanssssssssssssssss/plena-software/blob/main/docs/RESULTS.md)。

先看 [2026-10-04 验证汇总](../docs/VALIDATION.md)，再按下表查看原始记录。

| 目录 | 内容 |
|---|---|
| [fresh-clone/modules](repository-validation-2026-10-04/fresh-clone/modules) | RTL-v6：四行 Softmax 2 项测试、packed PV 1 项测试的日志、XML 和计时记录 |
| [fresh-clone/baseline](repository-validation-2026-10-04/fresh-clone/baseline) | 公开基线：小 Linear 生成、RTL 仿真、golden 对照、lint、运行配置及产物哈希 |
| [local](repository-validation-2026-10-04/local) | 整理过程中的本地检查；保留首次失败和后续重跑记录 |
| [history-2026-10-04](history-2026-10-04) | 仓库拆分前的归档，含上游 XML 和初次本机检查，也保留早期软件日志 |

本机复测的 128/128 来自 [Linear 日志](repository-validation-2026-10-04/fresh-clone/baseline/linear.log)：全部输出在既定容差内通过。模块测试与 Linear 使用不同工程版本，配置见[验证汇总](../docs/VALIDATION.md)。

[复测 manifest](repository-validation-2026-10-04/manifest.json) 与[历史 manifest](history-2026-10-04/manifest.json)用于核对已保存文件。历史归档包含失败用例，其状态不由后续局部测试覆盖。自己运行脚本产生的新结果写入根目录 `runs/`。

软件编译 A/B 与系统指标的独立复测记录见[软件日志目录](https://github.com/Sanssssssssssssssss/plena-software/tree/main/evidence)。
