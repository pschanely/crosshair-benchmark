import argparse
import os
from multiprocessing import Pool
import subprocess
import sys
import time
from datetime import date
from pathlib import Path

root_dir = Path(__file__).resolve().parent.parent
benchmarks_dir = root_dir / "benchmarks"
default_output_fname = str(
    root_dir / ("out_baseline_" + date.today().strftime("%Y%m%d") + ".csv")
)

parser = argparse.ArgumentParser(description="Run CrossHair benchmarks")
parser.add_argument(
    "-t", "--timeout", help="Maximum condition checking timeout", default=10 * 60
)
parser.add_argument(
    "-p", "--parallel",
    type=int,
    help="Amount of parallelism",
    default=max(1, (os.cpu_count() or 1) - 2)
)
parser.add_argument(
    "-o", "--output", help="Csv file for benchmark data", default=default_output_fname
)
args = parser.parse_args()

if Path(args.output).exists():
    print("Output file already exists. Please remove it first.")
    sys.exit(1)

timeout = args.timeout
basecmd = [
    sys.executable,
    "-m",
    "crosshair",
    "check",
    f"--per_condition_timeout={timeout}",
    f"--per_path_timeout={timeout ** 0.5}",
]

def run_file(benchmark_file: Path) -> tuple[str, float, int, str]:
    benchmark_name = "/".join(benchmark_file.parts[-2:])
    t0 = time.monotonic()
    cmd = basecmd + [str(benchmark_file)]
    # print()
    proc = subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
    output = str(proc.communicate()[0])
    duration = time.monotonic() - t0
    code = proc.returncode
    # print(f"Running:  {' '.join(cmd)}")
    # print(f"Exit code: {code}")
    # print(f"Output: {output}")
    # print(f"{benchmark_name} : {duration}")
    trace = f"Run: {' '.join(cmd)}\nDuration: {duration}\nOutput: {output}\n"
    return (benchmark_name, duration, code, trace)

if __name__ == '__main__':
    timings = {}
    pool = Pool(args.parallel)
    benchmark_files = sorted(benchmarks_dir.glob("*/crosshair_*.py"))
    for benchmark_name, duration, code, trace in pool.imap_unordered(run_file, benchmark_files):
        timings[benchmark_name] = (code, duration)
        print()
        print(trace)


    with open(args.output, "w") as fh:
        for name, (code, duration) in sorted(timings.items()):
            fh.write(f"{name},{code},{duration}\n")

    print()
    print("Benchmarks complete")
