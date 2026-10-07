# Module 07: case and Arrays

## Learn
```bash
case "$cmd" in
  start) echo "Starting" ;;
  stop|halt) echo "Stopping" ;;
  *) echo "Unknown" ;;
esac

fruits=(apple mango banana)
echo "${fruits[0]}"        # first item
echo "${#fruits[@]}"       # how many
for f in "${fruits[@]}"; do echo "$f"; done
```

## Your turn
Read a word. `start` prints `Starting service`, `stop` prints `Stopping service`, anything else prints `Unknown command`.

Create `answer.sh` in this folder, then check from the repo root:
```bash
./check.sh 07
```
Stuck? Re-read the lesson, run your script by hand, and only then look at `solution.sh`.
