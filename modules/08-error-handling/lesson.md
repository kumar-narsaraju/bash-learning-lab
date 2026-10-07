# Module 08: Safe Scripts and Error Handling

## Learn
Put this near the top of serious scripts:
```bash
set -euo pipefail
```
- `-e` stop on the first failing command
- `-u` error on unset variables (catches typos)
- `-o pipefail` a failure inside a pipe counts

Check things yourself and exit with a code:
```bash
[[ -f "$f" ]] || { echo "Error: ..." >&2; exit 1; }
trap 'echo cleaning up' EXIT      # runs when the script ends
```
Send errors to **stderr** with `>&2`.

## Your turn
Read a file name. If the file does not exist print `Error: file not found` and `exit 1`; otherwise print `OK`.

Create `answer.sh` in this folder, then check from the repo root:
```bash
./check.sh 08
```
Stuck? Re-read the lesson, run your script by hand, and only then look at `solution.sh`.
