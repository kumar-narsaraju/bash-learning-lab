# Server Hardware Troubleshooting projects

Hands-on practice with realistic sample data (saved command output from real servers). Do them after Module 10.

1. **IPMI event log triage**: `sel.txt` is saved `ipmitool sel list` output from a BMC.
2. **Temperature and fan check**: `sensors.txt` is saved `ipmitool sensor` output with columns separated by ` | ` (name, value, unit, status).
3. **Disk health scan (SMART)**: `smart.txt` has one line per disk: `device reallocated pending model`.
4. **Memory ECC error finder**: `edac.txt` lines look like `DIMM_A1 ce=0 ue=0` (correctable and uncorrectable errors).

Run them in the browser on the website, or locally with `./check.sh hardware/<project>`.
