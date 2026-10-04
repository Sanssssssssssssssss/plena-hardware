# 从单算子到 Prefill 优化

完整软硬件学习路径见 [软件工程的阶段拆解](https://github.com/Sanssssssssssssssss/plena-software/blob/main/docs/PROJECT_JOURNEY.md)。硬件先按以下顺序走，代码链接见 [READING](READING.md)。

| 阶段 | 观察与判断 | 动作与验收 |
|---|---|---|
| 1. 建立数值闭环 | Linear 的错误可能来自量化、布局、DMA 或写回 | 跑公开基线 tiny Linear，逐项核对 golden、镜像、指令和 RTL 比较日志 |
| 2. 理解在线归一化 | 每个 key block 改变最大值后，旧分母与 PV 输出必须乘 alpha | 在软件仓库跑 float64 数学 reference，再读硬件 m/l 更新 |
| 3. 定位状态开销 | 通用标量路径反复搬 m/l，矩阵变快后它可能占更大比例 | 顺着 state bank → SIMD → row engine，看首块、尾行、依赖与 valid/ready |
| 4. 定位 PV 整形 | 中间 shift/add 和输出读改写占用指令和 SRAM | 读 packed writeback/accumulator；测试 overwrite、accumulate、地址、mask、上下文保持 |
| 5. 多行并行 | 独立 query 行可并行，同一行有递推依赖 | R4 测试包含 3 个 active rows 尾组及相邻周期发射；不要把吞吐 II=1 当作单操作延迟 1 |
| 6. 检查收益上限 | FFN、QK/PV、HBM 不会随 R 同比加速，SRAM banking 有面积代价 | 结合软件消融表比较 state-only/direct-PV/R1/R2/R4/R8；R16 是历史结构外推 |
| 7. 回到系统指标 | 模块通过只限制功能正确性，不直接给出系统 TPS/tokens/J | 记录 precision/tile/版本后，由经过校准的成本模型和 A100 历史输入计算 |

练习时先写下“改动后哪些量应不变”：有效矩阵算术、有效 token/head、地址范围、累加顺序和精度约束；再预测减少哪些 opcode、访存或停顿。失败先检查同 profile 的配置与依赖，保留失败日志。
