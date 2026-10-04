# RTL 环境与原生入口

使用 Linux 或 WSL Ubuntu。系统需 `python3-venv`、g++、make、Perl。README 的独立 `.venv` 安装 CPU Torch 与 cocotb/Verilator；也支持仓库根目录的 `.venv-wsl`。

公开基线入口需要 [just](https://github.com/casey/just)。本轮使用 1.58.0；例如 x86_64 Linux 可从其 GitHub release 下载官方静态二进制，在仓库根目录执行：

```bash
mkdir -p .cache/just
curl -fL https://github.com/casey/just/releases/download/1.58.0/just-1.58.0-x86_64-unknown-linux-musl.tar.gz -o .cache/just/just.tar.gz
tar -xzf .cache/just/just.tar.gz -C .venv/bin just
bash scripts/run_rtl.sh modules
bash scripts/run_rtl.sh baseline
```

两个 profile 顺序运行。`run_rtl.sh` 设定 `SIMTOP_TRACE=0` 避免巨大波形文件、4 个构建任务；PyPI wheel 需要 `VERILATOR_ROOT` 与局部 `CFG_CXXFLAGS_PCH_I=-include`，脚本自动处理。

## 原生构建与综合

根目录保留快照 [justfile](../justfile)、[原 README](upstream/README.md)、[tools/synopsys](../tools/synopsys)。公开基线的 [README](../reference/upstream-release/README.md)、[justfile](../reference/upstream-release/justfile)、Docker/Nix 文件也完整保留。

在公开基线目录，`just rtl-sim linear true --batch 4 --in-features 16 --out-features 32` 是本仓库 baseline 入口调用的原始 recipe。直接使用它时需要按原 README 激活环境；它会修改本工程 `configuration.svh` 的指令偏移。本仓库包装入口在 finally 中恢复原字节。

直接跑 Python 时 PYTHONPATH 应只指向所选工程的 `src/system/test:tools:PLENA_Tools:PLENA_Compiler`，不要混用另一个 profile 的依赖。硬件参数改变需重建。测试异常可能进入上游 pdb，包装入口使用非交互 stdin。

综合入口和工艺引用保留原样。本轮未执行 Synopsys DC；真实综合需工具许可、对应工艺库和站点环境配置，不能把已有校准系数视为刚跑出的面积/功耗结果。
