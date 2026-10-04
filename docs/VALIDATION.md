# 独立仓库验收 · 2026-10-04

完整双工程在新目录导入，并用全新 `git clone` 验收。两套工程共 1,434 个上游文件，没有 gitlink、空子模块或 LFS 指针。45 处核心注释的非注释字节与导入源码一致；本仓库文档链接和历史证据哈希通过检查。

| 全新克隆中的检查 | 条件与结果 | 证据 |
|---|---|---|
| RTL-v6 四行 Softmax | R4、VLEN8、E5M6、STATE_ENTRIES32；2 项通过，含 ACTIVE_ROWS=3 尾组和相邻周期发射 | [日志](../evidence/repository-validation-2026-10-04/fresh-clone/modules/softmax_row_engine.log) / [XML](../evidence/repository-validation-2026-10-04/fresh-clone/modules/softmax_row_engine-results.xml) |
| RTL-v6 packed PV | VLEN8、BLEN4、E5M6；1 项通过，覆盖 overwrite/accumulate、地址、mask 和上下文保持 | [日志](../evidence/repository-validation-2026-10-04/fresh-clone/modules/packed_pv_writeback.log) / [XML](../evidence/repository-validation-2026-10-04/fresh-clone/modules/packed_pv_writeback-results.xml) |
| 公开基线 Linear | `(4,16)@(16,32)`，seed42；MLEN/VLEN/BLEN=8/8/4，MXINT8、内部 FP E6M5；158 个机器码字，cocotb 1 项通过 | [完整生成/仿真/比较日志](../evidence/repository-validation-2026-10-04/fresh-clone/baseline/linear.log) / [XML](../evidence/repository-validation-2026-10-04/fresh-clone/baseline/linear-results.xml) |
| 基线 VRAM 对照 | 128 个元素，100% 匹配；MSE=7.664934e-3，MAE=0.0662365，max error=0.295410 | 同一 Linear 日志中的 Verification Summary |
| 公开基线 RTL lint | standard SimTop lint clean | [lint 日志](../evidence/repository-validation-2026-10-04/fresh-clone/baseline/lint.log) |

数值比较沿用上游 `|err| <= 0.1 + 0.1*|golden|`、匹配率至少 90% 的门槛；这里的 100% 表示全部元素在容差内，不是 bit-exact。Linear 的验证配置选择 VRAM 比较，不据此声称所有 HBM/KV 数据通路已验证。

新克隆复用本仓库独立 Linux Python 3.12 工具环境（通过被忽略的本地 venv 链接），没有调用归档工程源码。Torch 2.7.1 CPU、cocotb 1.9.2、Verilator 5.34.0、just 1.58.0。模块主机耗时约 125.28s / 55.68s，最终 Linear 约 141.78s，含构建与验证；它们不是目标 NPU 延迟。[模块收据](../evidence/repository-validation-2026-10-04/fresh-clone/modules/receipt.json)、[Linear 收据](../evidence/repository-validation-2026-10-04/fresh-clone/baseline/receipt.json)。

源码版本按 [配套表](COMPATIBILITY.md) 固定；模块/lint 的包装工程 commit 为 `2fa3a8b`，最终 baseline 为 `aa37024`。中间补齐 PyYAML 安装依赖，并增强包装入口：移除旧 XML、检查新 XML、保存运行时配置、恢复原始配置。初次缺依赖日志保留，最终重跑通过。RTL 计算逻辑、上游 runner flags 和数值门槛未改动。

[运行时配置](../evidence/repository-validation-2026-10-04/fresh-clone/baseline/configuration-during-run.svh)、[精度](../evidence/repository-validation-2026-10-04/fresh-clone/baseline/precision.svh)、[验证参数](../evidence/repository-validation-2026-10-04/fresh-clone/baseline/verification_params.json)、[生成产物哈希](../evidence/repository-validation-2026-10-04/fresh-clone/baseline/generated-artifacts.json)及[证据 manifest](../evidence/repository-validation-2026-10-04/manifest.json)可追溯本次检查。

未运行完整 RTL 回归、RTL-v6 full-core 长上下文、DC 综合、GPU 或完整 DSE。历史包的 17 份 XML、29 个 testcase、4 个失败仍保留其原始状态；不得用这些局部新测试覆盖历史失败记录。
