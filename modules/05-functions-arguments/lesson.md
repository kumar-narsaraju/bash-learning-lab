# Module 05: Functions and Arguments

## Learn
```bash
greet() {            # define
  local who="$1"     # $1 = first argument, local = stays inside the function
  echo "Hello $who"
}
greet "Ravi"         # call
echo "$#"            # number of script arguments
echo "$@"            # all arguments
```
Scripts take arguments the same way: `./script.sh a b` makes `$1=a`, `$2=b`.
Functions "return" text by printing it; capture with `$(func)`.

## Your turn
The script receives two numbers as arguments (see `args.txt`). Write an `add` function and print `Sum: 7` for `3 4`.

Create `answer.sh` in this folder, then check from the repo root:
```bash
./check.sh 05
```
Stuck? Re-read the lesson, run your script by hand, and only then look at `solution.sh`.
