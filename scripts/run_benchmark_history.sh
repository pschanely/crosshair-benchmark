#!/bin/bash

set -e

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd $SCRIPT_DIR
pyenv local 3.10.11
git clone https://github.com/pschanely/CrossHair.git
cd CrossHair

for VER in \
    v0.0.20 v0.0.21 v0.0.22 v0.0.23 v0.0.24 \
    v0.0.25 v0.0.26 v0.0.27 v0.0.28 v0.0.29 \
    v0.0.30 v0.0.31 v0.0.32 v0.0.33 v0.0.34 \
    v0.0.35 v0.0.36 v0.0.37 v0.0.38 v0.0.39 \
    v0.0.40 v0.0.41 v0.0.42 v0.0.43 v0.0.44 \
    v0.0.45 v0.0.46 v0.0.47 v0.0.48 v0.0.49 \
    v0.0.50 v0.0.51 v0.0.52 v0.0.53 v0.0.54 \
    v0.0.55 v0.0.56 v0.0.57 v0.0.58 v0.0.59 \
    v0.0.60 v0.0.61 v0.0.62 v0.0.63 v0.0.64 \
    v0.0.65 v0.0.66 v0.0.67 v0.0.68 v0.0.69 \
    v0.0.70 v0.0.71 v0.0.72 v0.0.73 v0.0.74
do
    if [ ! -f "../out_baseline_${VER}.csv" ]; then
        git checkout tags/${VER}
        pyenv exec pip install .[dev]
        pyenv exec python ../run_benchmarks.py -o "../out_baseline_${VER}.csv"
        git switch -
    fi
done

cd ..
rm -rf CrossHair
