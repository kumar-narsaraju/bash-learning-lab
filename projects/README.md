# Projects: build real tools

**Career tracks (with sample data, checked automatically):**
- [Data Center System Administration](datacenter/README.md): rack inventory, disk alerts, SSH attack logs, patch lists
- [Server Hardware Troubleshooting](hardware/README.md): IPMI event log, fans/temps, SMART disks, ECC memory

They also run in the browser on the website. Maintainers: edit `tools/gen_projects.py`, then run `python3 tools/gen_projects.py && python3 tools/build_site.py`.

Do these after Module 10. Start from `templates/script-template.sh`. Write your plan in comments first.

1. **backup.sh**: copy a folder into `backup-YYYY-MM-DD.tar.gz` (`tar -czf`, `date +%F`); refuse to run if the source is missing; keep only the last 5 backups.
2. **sysreport.sh**: print hostname, uptime, disk use (`df -h`), memory (`free -h`), top 5 processes (`ps aux --sort=-%mem | head`). Save to a dated file.
3. **logscan.sh**: given a log file, count lines containing ERROR/WARN, print the 5 most frequent error messages (`grep`, `sort | uniq -c | sort -rn | head`).
4. **menu.sh**: an interactive menu with `select`/`case` that runs the tools above.
5. **Your idea**: automate something you do by hand every week.

Share yours: fork the repo, add it to `community/`, open a pull request.
