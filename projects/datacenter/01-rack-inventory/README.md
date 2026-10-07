# Rack inventory report

**Goal:** Your asset list `inventory.csv` has columns `hostname,rack,u,role,status`. Print how many servers sit in each rack (format `R01: 3`), then a line `NOT ONLINE:` followed by the hostnames whose status is not `online`.

**Hint:** `cut`, `sort | uniq -c`, `awk -F,`. Skip the header line with `tail -n +2`.

Sample data: `inventory.csv`. Write `answer.sh` in this folder and check it with `./check.sh datacenter/01-rack-inventory`.
