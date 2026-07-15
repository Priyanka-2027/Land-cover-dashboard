"""
Run all script-style test_*.py files as standalone scripts (not via pytest).
This helps run tests that are written as executable scripts rather than pytest functions.
"""
import subprocess
import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent

def run_script(path: Path) -> int:
    print('\n' + '='*80)
    print(f"Running {path.relative_to(project_root)}")
    print('='*80)
    proc = subprocess.run([sys.executable, str(path)], cwd=str(project_root))
    return proc.returncode


def main():
    tests = sorted(project_root.glob('test_*.py'))
    if not tests:
        print('No script-style test_*.py files found.')
        return 0

    failures = []
    for t in tests:
        rc = run_script(t)
        if rc != 0:
            failures.append((t.name, rc))
            print(f"FAILED: {t.name} (exit {rc})")
        else:
            print(f"PASSED: {t.name}")

    print('\n' + '='*80)
    if failures:
        print('Some script tests failed:')
        for name, rc in failures:
            print(f" - {name}: exit {rc}")
        return 1
    else:
        print('All script-style tests passed.')
        return 0

if __name__ == '__main__':
    sys.exit(main())
