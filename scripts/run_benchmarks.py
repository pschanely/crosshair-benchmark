import argparse
import subprocess
import os
from pathlib import Path
import sys
import time

benchmarks_dir = Path(__file__).parent.parent / "benchmarks"

print(benchmarks_dir.absolute())
parser = argparse.ArgumentParser(description='Run CrossHair benchmarks')
parser.add_argument('-t', '--timeout', help='Maximum condition checking timeout', default=10*60)
parser.add_argument('-o', '--output', help="Csv file for benchmark data", default="out.csv")
args = parser.parse_args()

if Path(args.output).exists():
    print("Output file already exists. Please remove it first.")
    sys.exit(1)

timings = {}

basecmd = ["crosshair", "check", f"--per_condition_timeout={args.timeout}"]
for benchmark_file in sorted(benchmarks_dir.glob("*/crosshair_*.py")):
    benchmark_name = "/".join(benchmark_file.parts[-2:])
    t0 = time.monotonic()
    cmd = basecmd + [str(benchmark_file)]
    print()
    print(f"Running:  {' '.join(cmd)}")
    proc = subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
    output = proc.communicate()[0]
    duration = time.monotonic() - t0
    code = proc.returncode
    print(f"Exit code: {code}")
    print(f"Output: {output}")
    print(f"{benchmark_name} : {duration}")
    timings[benchmark_name] = (code, duration)

with open(args.output, "w") as fh:
    for name, (code, duration) in sorted(timings.items()):
        fh.write(f"{name},{code},{duration}\n")

print()
print("Benchmarks complete")
