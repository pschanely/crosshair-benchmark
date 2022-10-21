import glob
from collections import defaultdict

runs = defaultdict(dict)
first_times = {}
filenames = sorted(glob.glob("./out_baseline_*.csv"))
# print(filenames)
for filename in filenames:
    with open(filename) as fh:
        run = runs[filename]
        for line in fh.readlines():
            name, code, secs = line.split(",")
            secs = float(secs)
            # print(name, secs)
            run[name] = secs
            if name not in first_times:
                first_times[name] = secs
        runs[filename] = run


def avg(values):
    return sum(values) / len(values)


# print(runs.keys())
curkeys = list(runs[list(runs.keys())[-1]].keys())
# print(curkeys)


def date_of_file(filename: str) -> str:
    return filename.removeprefix("./out_baseline_").removesuffix(".csv")


print(" ".join([f"{date_of_file(filename)}" for filename in filenames]))
for name in first_times.keys():
    print(
        "",
        "  ".join(
            [
                f"{runs[filename].get(name, float('nan')):07.3f}"
                for filename in filenames
            ]
        ),
        " ",
        name,
    )


print()

for filename in filenames:
    # print(filename, runs[filename])
    # print([runs[filename].get(k, first_times[k]) for k in curkeys])
    avgtime = avg([runs[filename].get(k, first_times[k]) for k in curkeys])
    dt = date_of_file(filename)
    print(f"{dt} : {avgtime}")
