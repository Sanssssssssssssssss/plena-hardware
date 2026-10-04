#!/usr/bin/env bash
# Run from any directory: bash scripts/run_rtl.sh [modules|baseline]
set -euo pipefail
ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
if [[ -f "$ROOT/.venv-wsl/bin/activate" ]]; then
    source "$ROOT/.venv-wsl/bin/activate"
elif [[ -f "$ROOT/.venv/bin/activate" ]]; then
    source "$ROOT/.venv/bin/activate"
else
    echo 'Create a Linux/WSL venv as described in README.md' >&2
    exit 1
fi
WHEEL_ROOT=$(python -c 'import sysconfig; print(sysconfig.get_paths()["purelib"] + "/verilator")')
if [[ -x "$WHEEL_ROOT/bin/verilator" ]]; then
    export VERILATOR_ROOT="$WHEEL_ROOT"
    export PATH="$VERILATOR_ROOT/bin:$PATH"
    # PyPI 5.34.0 wheel omits GCC's precompiled-header include flag.
    export MAKEFLAGS="-j4 CFG_CXXFLAGS_PCH_I=-include"
fi
export VERILATOR_JOBS=4 SIMTOP_TRACE=0 PYTHONUTF8=1
python "$ROOT/scripts/run_rtl.py" "${1:-modules}"
