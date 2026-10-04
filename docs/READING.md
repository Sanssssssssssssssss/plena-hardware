# 核心代码阅读索引

以下链接直接进入工程源码。注释解释数据布局、状态递推、调度取舍和验证断言，保留原有计算逻辑。两仓库合计 88 处；本仓库 45 处。

| 实际文件 | 新增核心注释 |
|---|---:|
| [reference/upstream-release/tools/testworkloads/linear.py](../reference/upstream-release/tools/testworkloads/linear.py) | 8 |
| [src/vector_machine/rtl/softmax_state_bank.sv](../src/vector_machine/rtl/softmax_state_bank.sv) | 5 |
| [src/vector_machine/rtl/softmax_state_simd.sv](../src/vector_machine/rtl/softmax_state_simd.sv) | 6 |
| [src/vector_machine/rtl/softmax_row_engine.sv](../src/vector_machine/rtl/softmax_row_engine.sv) | 9 |
| [src/matrix_machine/rtl/packed_pv_writeback.sv](../src/matrix_machine/rtl/packed_pv_writeback.sv) | 6 |
| [src/matrix_machine/rtl/packed_pv_accumulator.sv](../src/matrix_machine/rtl/packed_pv_accumulator.sv) | 5 |
| [src/vector_machine/test/softmax_row_engine_tb.py](../src/vector_machine/test/softmax_row_engine_tb.py) | 6 |

按 [项目阶段](PROJECT_JOURNEY.md) 阅读，并在每个阶段保存自己的配置、预测和观测。别把指令数、模拟周期、目标时延和主机运行秒数混成一个指标。
