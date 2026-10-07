# Disk health scan (SMART)

**Goal:** `smart.txt` has one line per disk: `device reallocated pending model`. A disk is FAILING if reallocated > 0 or pending > 0. Print `FAILING <device> (realloc=<r> pending=<p>)` for those, then `Healthy disks: <n>`.

**Hint:** awk: `if ($2>0 || $3>0) {...} else h++` and print `h+0` at the end.

Sample data: `smart.txt`. Write `answer.sh` in this folder and check it with `./check.sh hardware/03-disk-health-scan`.
