# Module 06: Working with Text

## Learn
The Linux toolbox, connected with **pipes** (`|`):
```bash
grep "error" log.txt          # find lines
cut -d, -f2 data.csv          # column 2 of a CSV
sort | uniq -c                # count duplicates
wc -l file.txt                # count lines
sed 's/old/new/g' file.txt    # replace text
awk -F, '{s+=$2} END{print s}' data.csv   # sum a column
```
`>` writes a file, `>>` appends, `<` feeds a file in. `2>` redirects errors.

## Your turn
Input lines look like `name,score`. Print `Total: ` followed by the sum of all scores.

Create `answer.sh` in this folder, then check from the repo root:
```bash
./check.sh 06
```
Stuck? Re-read the lesson, run your script by hand, and only then look at `solution.sh`.
