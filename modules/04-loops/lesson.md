# Module 04: Loops

## Learn
```bash
for i in {1..5}; do echo "$i"; done
for f in *.txt; do echo "$f"; done
i=0; while (( i < 3 )); do echo "$i"; ((i++)); done
while read -r line; do echo "got: $line"; done < file.txt
```
`break` leaves a loop, `continue` skips to the next round.

## Your turn
Print the squares of 1 to 5, one per line, like `3 squared is 9`.

Create `answer.sh` in this folder, then check from the repo root:
```bash
./check.sh 04
```
Stuck? Re-read the lesson, run your script by hand, and only then look at `solution.sh`.
