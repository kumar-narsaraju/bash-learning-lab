# Patch and reboot list

**Goal:** `servers.txt` has lines `hostname uptime_days kernel`. Servers up more than 90 days need a reboot window. Print `REBOOT <hostname> (<days> days)` for each, then `Total: <n>`.

**Hint:** awk with a counter: `$2>90 {print ...; n++} END {print "Total:", n+0}`.

Sample data: `servers.txt`. Write `answer.sh` in this folder and check it with `./check.sh datacenter/04-patch-and-reboot-list`.
