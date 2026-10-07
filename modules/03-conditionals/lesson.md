# Module 03: Making Decisions (if)

## Learn
```bash
if [[ -f "$file" ]]; then echo "file exists"
elif [[ -d "$file" ]]; then echo "directory"
else echo "missing"; fi

if (( n % 2 == 0 )); then echo even; fi
```
Tests: `-f` file, `-d` directory, `-z` empty string, `==` string equal. For numbers use `(( ))` with `< > ==` or `-lt -gt -eq` inside `[[ ]]`.
Every command returns an **exit code**: `0` = success, anything else = failure. `$?` holds the last one.

## Your turn
Read a number. Print `N is even` or `N is odd`.

Create `answer.sh` in this folder, then check from the repo root:
```bash
./check.sh 03
```
Stuck? Re-read the lesson, run your script by hand, and only then look at `solution.sh`.
