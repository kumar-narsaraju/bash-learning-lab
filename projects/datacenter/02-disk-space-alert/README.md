# Disk space alert

**Goal:** `df.txt` is saved `df -h` output. Print `ALERT <mount> <percent>` for every filesystem that is 80% full or more. Nothing else.

**Hint:** Percent is column 5 (`85%`). In awk, `+$5` turns `85%` into the number 85. Mount is column 6.

Sample data: `df.txt`. Write `answer.sh` in this folder and check it with `./check.sh datacenter/02-disk-space-alert`.
