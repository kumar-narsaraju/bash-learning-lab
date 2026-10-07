# Temperature and fan check

**Goal:** `sensors.txt` is saved `ipmitool sensor` output with columns separated by ` | ` (name, value, unit, status). Print `CHECK <name>: <value> <unit>` for every sensor whose status is not `ok`.

**Hint:** `awk -F' \\| '` splits on the pipe. Status is field 4.

Sample data: `sensors.txt`. Write `answer.sh` in this folder and check it with `./check.sh hardware/02-temperature-and-fans`.
