import enum, glob, sys, math
from collections import defaultdict

class AnsiColor(enum.Enum):
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

def color(text: str, *effects: AnsiColor) -> str:
    if not effects:
        return text
    return "".join(getattr(e, "value", str(e)) for e in effects) + text + AnsiColor.ENDC.value

runs: dict[str, dict[str, float]] = defaultdict(dict)
first_times = {}
if len(sys.argv) > 1:
    filenames = sys.argv[1:]
else:
    filenames = sorted(glob.glob("./out_baseline_*.csv"))
# print(filenames)
for filename in filenames:
    with open(filename) as fh:
        run = runs[filename]
        for line in fh.readlines():
            name, code, secstr = line.split(",")
            secs = float(secstr)
            if code not in ("0", "1"):
                print(f"Unexpected response code ({code}) found in {name} @ {filename}")
                secs = 999
            run[name] = secs
            if name not in first_times:
                first_times[name] = secs
        runs[filename] = run


# print(runs.keys())
curkeys = list(runs[list(runs.keys())[-1]].keys())
# print(curkeys)
keybuckets = set(k.split("/")[0] for k in curkeys)

def date_of_file(filename: str) -> str:
    return filename.removeprefix("./out_baseline_").removesuffix(".csv")

def avg(samples):
    samples = [s for s in samples if not math.isnan(s)]
    if len(samples) == 0:
        return float('nan')
    return sum(samples) / len(samples)

print("  ".join([f"{date_of_file(filename)}" for filename in filenames]))
for name in first_times.keys():
    for fidx, filename in enumerate(filenames):
        runtime = runs[filename].get(name, float('nan'))
        colors = []
        if fidx > 0:
            prevs = [runs[filenames[i]].get(name, float('nan')) for i in range(max(fidx-20, 0), fidx)]
            prevtime = avg(prevs)#runs[filenames[fidx-1]].get(name, float('nan'))
            # print(prevtime, runtime)
            if not math.isnan(prevtime):
                delta = runtime / prevtime
                if delta < 0.33:
                    colors = [AnsiColor.OKGREEN]
                elif delta < 0.66:
                    colors = [AnsiColor.OKBLUE]
                elif delta > 1.66:
                    colors = [AnsiColor.FAIL]
                elif delta > 1.33:
                    colors = [AnsiColor.WARNING]
        print(color(f"{runtime:07.3f}", *colors), "  ", end='')
    print(name)


print()

for filename in filenames:
    bucketscores = defaultdict(list)
    for key in curkeys:
        bucket = key.split("/")[0]
        bucketscores[bucket].append(runs[filename].get(key, first_times[key]))
        # bucketscores[bucket].append((runs[filename].get(key, first_times[key]) + 1.0) ** 0.5)
    # print(filename, runs[filename])
    # print([runs[filename].get(k, first_times[k]) for k in curkeys])
    # avgtime = avg([sum(scores)/len(scores) for scores in bucketscores.values()])
    avgtime = avg([sum(s**0.5 for s in scores)/len(scores) for scores in bucketscores.values()])
    # tottime = sum([ (len(scores)**0.5)*sum(scores)/len(scores) for scores in bucketscores.values()])
    # avgtime = tottime / sum([len(scores)**0.5 for scores in bucketscores.values()])
    dt = date_of_file(filename)
    print(f"{dt}, {avgtime}")
