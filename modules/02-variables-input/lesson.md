# Module 02: Variables and Input

## Learn
```bash
name="Asha"          # no spaces around =
echo "Hi $name"      # use $ to read; double quotes keep spaces safe
read -r city         # read a line typed by the user
echo $((2 + 3))      # arithmetic with $(( ))
today=$(date +%F)    # command substitution: store a command's output
```
**Always quote variables** (`"$name"`). Unquoted variables break on spaces.

## Your turn
Read a name, then an age (two lines of input). Print: `Hi NAME, next year you will be AGE+1.`

Create `answer.sh` in this folder, then check from the repo root:
```bash
./check.sh 02
```
Stuck? Re-read the lesson, run your script by hand, and only then look at `solution.sh`.
