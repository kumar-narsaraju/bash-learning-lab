# Module 01: Your First Script

## Learn
A script is a text file of commands. Bash runs them top to bottom.

```bash
#!/usr/bin/env bash
echo "Hello"
```
- `#!/usr/bin/env bash` (the **shebang**) tells Linux which program runs the file.
- `echo` prints text.
- Run it: `bash answer.sh`, or `chmod +x answer.sh` then `./answer.sh`.
- Lines starting with `#` are comments. Use them.

## Your turn
Print exactly two lines:
```
Hello, Linux!
I am learning Bash.
```

Create `answer.sh` in this folder, then check from the repo root:
```bash
./check.sh 01
```
Stuck? Re-read the lesson, run your script by hand, and only then look at `solution.sh`.
