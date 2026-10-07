# IPMI event log triage

**Goal:** `sel.txt` is saved `ipmitool sel list` output from a BMC. Print only the events that mention `Critical` or `Uncorrectable`, then a final line `Critical events: <n>`.

**Hint:** `grep -E 'Critical|Uncorrectable'` and `wc -l`. Count first with a variable.

Sample data: `sel.txt`. Write `answer.sh` in this folder and check it with `./check.sh hardware/01-ipmi-event-triage`.
