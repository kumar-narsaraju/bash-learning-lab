#!/usr/bin/env python3
"""Generates projects/<track>/<NN-name>/ (README.md, sample data, solution.sh, expected.txt).
expected.txt is produced by running solution.sh with real bash, so it can never drift."""
import os, subprocess, tempfile, shutil
T = {
 "datacenter": "Data Center System Administration",
 "hardware": "Server Hardware Troubleshooting",
}
P = [
# ---------------- data center sysadmin ----------------
dict(track="datacenter", id="01-rack-inventory", title="Rack inventory report",
 goal="Your asset list `inventory.csv` has columns `hostname,rack,u,role,status`. Print how many servers sit in each rack (format `R01: 3`), then a line `NOT ONLINE:` followed by the hostnames whose status is not `online`.",
 hint="`cut`, `sort | uniq -c`, `awk -F,`. Skip the header line with `tail -n +2`.",
 files={"inventory.csv": "hostname,rack,u,role,status\nweb01,R01,10,web,online\nweb02,R01,11,web,online\ndb01,R01,20,database,maintenance\ngpu01,R02,5,gpu,online\ngpu02,R02,7,gpu,offline\nstor01,R03,2,storage,online\n"},
 sol='''#!/usr/bin/env bash
tail -n +2 inventory.csv | cut -d, -f2 | sort | uniq -c | awk '{print $2": "$1}'
echo "NOT ONLINE:"
tail -n +2 inventory.csv | awk -F, '$5!="online"{print $1}'
'''),
dict(track="datacenter", id="02-disk-space-alert", title="Disk space alert",
 goal="`df.txt` is saved `df -h` output. Print `ALERT <mount> <percent>` for every filesystem that is 80% full or more. Nothing else.",
 hint="Percent is column 5 (`85%`). In awk, `+$5` turns `85%` into the number 85. Mount is column 6.",
 files={"df.txt": "Filesystem      Size  Used Avail Use% Mounted on\n/dev/sda2        50G   41G  9.0G  82% /\n/dev/sdb1       2.0T  1.1T  900G  55% /data\n/dev/sdc1       4.0T  3.8T  200G  95% /backup\ntmpfs           16G     0   16G   0% /dev/shm\n"},
 sol='''#!/usr/bin/env bash
awk 'NR>1 && +$5>=80 {print "ALERT", $6, $5}' df.txt
'''),
dict(track="datacenter", id="03-failed-ssh-logins", title="Failed SSH login hunter",
 goal="`auth.log` is a login log. Print the source IPs of `Failed password` lines with their counts, most attempts first, as `<count> <ip>`.",
 hint="`grep 'Failed password'`, then pull the IP (the word after `from`), then `sort | uniq -c | sort -rn`.",
 files={"auth.log": "Oct  7 01:02:11 srv sshd[411]: Failed password for root from 203.0.113.9 port 4022 ssh2\nOct  7 01:02:14 srv sshd[411]: Failed password for root from 203.0.113.9 port 4023 ssh2\nOct  7 01:05:40 srv sshd[502]: Accepted password for admin from 10.0.0.5 port 5100 ssh2\nOct  7 01:09:01 srv sshd[611]: Failed password for invalid user test from 198.51.100.7 port 3111 ssh2\nOct  7 01:09:05 srv sshd[611]: Failed password for root from 203.0.113.9 port 4030 ssh2\n"},
 sol='''#!/usr/bin/env bash
grep 'Failed password' auth.log | awk '{for(i=1;i<=NF;i++) if($i=="from") print $(i+1)}' | sort | uniq -c | sort -rn | awk '{print $1, $2}'
'''),
dict(track="datacenter", id="04-patch-and-reboot-list", title="Patch and reboot list",
 goal="`servers.txt` has lines `hostname uptime_days kernel`. Servers up more than 90 days need a reboot window. Print `REBOOT <hostname> (<days> days)` for each, then `Total: <n>`.",
 hint="awk with a counter: `$2>90 {print ...; n++} END {print \"Total:\", n+0}`.",
 files={"servers.txt": "web01 12 5.15.0-91\nweb02 140 5.15.0-60\ndb01 95 5.15.0-60\ngpu01 30 5.15.0-91\nstor01 400 5.4.0-100\n"},
 sol='''#!/usr/bin/env bash
awk '$2>90 {print "REBOOT", $1, "(" $2 " days)"; n++} END {print "Total:", n+0}' servers.txt
'''),
# ---------------- hardware troubleshooting ----------------
dict(track="hardware", id="01-ipmi-event-triage", title="IPMI event log triage",
 goal="`sel.txt` is saved `ipmitool sel list` output from a BMC. Print only the events that mention `Critical` or `Uncorrectable`, then a final line `Critical events: <n>`.",
 hint="`grep -E 'Critical|Uncorrectable'` and `wc -l`. Count first with a variable.",
 files={"sel.txt": "1 | 10/05/2026 | 02:11:09 | Temperature CPU1 | Upper Critical going high | Asserted\n2 | 10/05/2026 | 02:14:31 | Fan FAN3 | Lower Non-recoverable going low | Asserted\n3 | 10/06/2026 | 11:00:00 | Power Supply PS2 | Presence detected | Deasserted\n4 | 10/06/2026 | 11:00:05 | Memory DIMM_B2 | Uncorrectable ECC | Asserted\n5 | 10/07/2026 | 06:30:12 | Drive Slot Bay4 | Drive Fault | Asserted\n"},
 sol='''#!/usr/bin/env bash
grep -E 'Critical|Uncorrectable' sel.txt
n=$(grep -cE 'Critical|Uncorrectable' sel.txt)
echo "Critical events: $n"
'''),
dict(track="hardware", id="02-temperature-and-fans", title="Temperature and fan check",
 goal="`sensors.txt` is saved `ipmitool sensor` output with columns separated by ` | ` (name, value, unit, status). Print `CHECK <name>: <value> <unit>` for every sensor whose status is not `ok`.",
 hint="`awk -F' \\\\| '` splits on the pipe. Status is field 4.",
 files={"sensors.txt": "CPU1 Temp | 92.000 | degrees C | cr\nCPU2 Temp | 61.000 | degrees C | ok\nFAN1 | 8400.000 | RPM | ok\nFAN3 | 0.000 | RPM | cr\nPS1 Status | 0x1 | discrete | ok\nInlet Temp | 38.000 | degrees C | nc\n"},
 sol='''#!/usr/bin/env bash
awk -F' \\\\| ' '$4!="ok" {print "CHECK " $1 ": " $2 " " $3}' sensors.txt
'''),
dict(track="hardware", id="03-disk-health-scan", title="Disk health scan (SMART)",
 goal="`smart.txt` has one line per disk: `device reallocated pending model`. A disk is FAILING if reallocated > 0 or pending > 0. Print `FAILING <device> (realloc=<r> pending=<p>)` for those, then `Healthy disks: <n>`.",
 hint="awk: `if ($2>0 || $3>0) {...} else h++` and print `h+0` at the end.",
 files={"smart.txt": "/dev/sda 0 0 Samsung_PM883\n/dev/sdb 12 0 Seagate_ST4000\n/dev/sdc 0 3 WDC_WD4003\n/dev/sdd 0 0 Samsung_PM883\n"},
 sol='''#!/usr/bin/env bash
awk '{ if ($2>0 || $3>0) print "FAILING", $1, "(realloc=" $2 " pending=" $3 ")"; else h++ } END {print "Healthy disks:", h+0}' smart.txt
'''),
dict(track="hardware", id="04-memory-ecc-errors", title="Memory ECC error finder",
 goal="`edac.txt` lines look like `DIMM_A1 ce=0 ue=0` (correctable and uncorrectable errors). Replace a DIMM when ue>0 or ce>100. Print `REPLACE <dimm>` for those, one per line.",
 hint="Remove the `ce=`/`ue=` text with `sed` or use awk `split($2,a,\"=\")`.",
 files={"edac.txt": "DIMM_A1 ce=0 ue=0\nDIMM_A2 ce=250 ue=0\nDIMM_B1 ce=3 ue=0\nDIMM_B2 ce=10 ue=1\n"},
 sol='''#!/usr/bin/env bash
sed 's/ce=//; s/ue=//' edac.txt | awk '$3>0 || $2>100 {print "REPLACE", $1}'
'''),
]
root = "projects"
for p in P:
    d = f"{root}/{p['track']}/{p['id']}"
    shutil.rmtree(d, ignore_errors=True); os.makedirs(d)
    for n, c in p["files"].items(): open(f"{d}/{n}", "w").write(c)
    open(f"{d}/solution.sh", "w").write(p["sol"])
    r = subprocess.run(["bash", "solution.sh"], cwd=d, capture_output=True, text=True)
    assert r.returncode == 0 and r.stdout.strip(), (p["id"], r.stderr)
    open(f"{d}/expected.txt", "w").write(r.stdout)
    open(f"{d}/README.md", "w").write(f"# {p['title']}\n\n**Goal:** {p['goal']}\n\n**Hint:** {p['hint']}\n\nSample data: {', '.join('`'+f+'`' for f in p['files'])}. Write `answer.sh` in this folder and check it with `./check.sh {p['track']}/{p['id']}`.\n")
    print("ok", d); print(r.stdout)
for t, name in T.items():
    items = [p for p in P if p["track"] == t]
    open(f"{root}/{t}/README.md", "w").write(f"# {name} projects\n\nHands-on practice with realistic sample data (saved command output from real servers). Do them after Module 10.\n\n" + "".join(f"{i+1}. **{p['title']}**: {p['goal'].split('. ')[0]}.\n" for i, p in enumerate(items)) + "\nRun them in the browser on the website, or locally with `./check.sh " + t + "/<project>`.\n")
