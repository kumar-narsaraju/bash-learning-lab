# Module 09: Logging and Automation

## Learn
```bash
log() { echo "[INFO] $*"; }
log "Backup started"
echo "$(date '+%F %T') done" >> run.log     # timestamped log line
```
**cron** runs scripts on a schedule. Edit with `crontab -e`:
```
# min hour day month weekday  command
30 2 * * *  /home/me/backup.sh >> /home/me/backup.log 2>&1
```
That means "every day at 02:30". Always use full paths in cron.

## Your turn
Read one line of text and print it as a log line: `[INFO] <text>`. Use a `log` function.

Create `answer.sh` in this folder, then check from the repo root:
```bash
./check.sh 09
```
Stuck? Re-read the lesson, run your script by hand, and only then look at `solution.sh`.
