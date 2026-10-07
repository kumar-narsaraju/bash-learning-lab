#!/usr/bin/env bash
# Usage: ./check.sh 01            checks modules/01-*/answer.sh
#        ./check.sh 01 --solution checks the reference solution
n="${1:-}"; mode="${2:-}"
# Projects: ./check.sh datacenter/01-rack-inventory  (runs inside the project folder, sample files are there)
if [[ $n == */* ]]; then
  pdir="projects/$n"; [[ -d $pdir ]] || { echo "No such project: $n"; exit 2; }
  ps="answer.sh"; [[ $mode == --solution ]] && ps="solution.sh"
  [[ -f $pdir/$ps ]] || { echo "Create $pdir/$ps first"; exit 2; }
  actual=$(cd "$pdir" && bash "$ps" 2>&1 || true); expected=$(cat "$pdir/expected.txt")
  if [[ $actual == "$expected" ]]; then echo "PASS  project $n"; else echo "FAIL  project $n"; echo "--- expected"; echo "$expected"; echo "--- got"; echo "$actual"; exit 1; fi
  exit 0
fi
dir=$(ls -d modules/"$n"-* 2>/dev/null | head -1)
[[ -n $dir ]] || { echo "No such module: $n"; exit 2; }
script="$dir/answer.sh"; [[ $mode == --solution ]] && script="$dir/solution.sh"
[[ -f $script ]] || { echo "Create $script first"; exit 2; }
args=(); [[ -f $dir/args.txt ]] && read -ra args < "$dir/args.txt"
actual=$(bash "$script" "${args[@]}" < "$dir/input.txt" 2>&1 || true)
expected=$(cat "$dir/expected.txt")
if [[ $actual == "$expected" ]]; then
  echo "PASS  module $n"
else
  echo "FAIL  module $n"; echo "--- expected"; echo "$expected"; echo "--- got"; echo "$actual"; exit 1
fi
