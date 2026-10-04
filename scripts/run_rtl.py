"""Sequential cocotb validation; XML is authoritative even if the runner exits 0."""
from pathlib import Path
import argparse
import json
import os
import subprocess
import sys
import time
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


def check_xml(path):
    tests = list(ET.parse(path).iter('testcase'))
    assert tests and all(t.find('failure') is None and t.find('error') is None
                         and t.find('skipped') is None for t in tests), path
    return len(tests)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('profile', choices=('modules', 'baseline'))
    args = parser.parse_args()
    project = ROOT if args.profile == 'modules' else ROOT / 'reference/upstream-release'
    out = ROOT / 'runs' / args.profile
    out.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ, PYTHONPATH=os.pathsep.join(str(project / p) for p in (
        'src/system/test', 'tools', 'PLENA_Tools', 'PLENA_Compiler')))
    receipt = {'profile': args.profile, 'jobs': {}}

    def run(name, command, timeout=900):
        started = time.perf_counter()
        with (out / (name + '.log')).open('w', encoding='utf-8') as log:
            result = subprocess.run(command, cwd=project, env=env, stdin=subprocess.DEVNULL,
                                    stdout=log, stderr=subprocess.STDOUT, timeout=timeout)
        receipt['jobs'][name] = {'exit_code': result.returncode, 'seconds': time.perf_counter() - started}
        (out / 'receipt.json').write_text(json.dumps(receipt, indent=2), encoding='utf-8')
        if result.returncode:
            raise RuntimeError(f'{name} failed; see {out / (name + ".log")}')

    if args.profile == 'modules':
        for name, group, wrapper in (
            ('softmax_row_engine', 'vector_machine', 'softmax_row_engine_test_wrapper'),
            ('packed_pv_writeback', 'matrix_machine', 'packed_pv_writeback'),
        ):
            xml = project / f'src/{group}/test/build/{wrapper}/test_0/results.xml'
            xml.unlink(missing_ok=True)
            run(name, [sys.executable, f'src/{group}/test/{name}_tb.py'])
            count = check_xml(xml)
            (out / (name + '-results.xml')).write_bytes(xml.read_bytes())
            receipt['jobs'][name]['passed_tests'] = count
            print(f'{name}: {count} tests PASS', flush=True)
    else:
        # Use the upstream recipe unchanged. Its generator owns the offset update.
        # Restore both success and failure paths to keep source hashes reproducible.
        configuration = project / 'src/definitions/configuration.svh'
        before = configuration.read_bytes()
        try:
            run('linear', ['just', 'rtl-sim', 'linear', 'true', '--batch', '4',
                           '--in-features', '16', '--out-features', '32'], timeout=1800)
            build = project / 'build/test/linear'
            assert (build / 'golden_result.pt').is_file()
            assert (build / 'hbm_result.mem').is_file()
            words = (build / 'generated_machine_code.mem').read_text().splitlines()
            assert words and all(0 <= int(w, 16) < 2**32 for w in words if w.strip())
            receipt['machine_code_words'] = len(words)
            for name in ('verification_params.json', 'comparison_params.json'):
                if (build / name).exists():
                    (out / name).write_bytes((build / name).read_bytes())
            print(f'Baseline Linear: simulation + upstream golden comparison PASS; {len(words)} words', flush=True)
        finally:
            configuration.write_bytes(before)
    (out / 'receipt.json').write_text(json.dumps(receipt, indent=2), encoding='utf-8')


if __name__ == '__main__':
    main()
