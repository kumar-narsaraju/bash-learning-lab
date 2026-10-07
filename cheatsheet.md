# Bash Cheatsheet
| Task | Syntax |
|---|---|
| Variable | `x="hi"`, read with `"$x"` |
| Math | `$((a + b))` |
| Input | `read -r var` |
| If | `if [[ cond ]]; then ...; fi` |
| For | `for i in {1..5}; do ...; done` |
| While | `while read -r l; do ...; done < file` |
| Function | `f() { local a="$1"; echo "$a"; }` |
| Args | `$1 $2`, `$#` count, `$@` all |
| Exit code | `$?`, `exit 1` |
| Redirect | `>` write, `>>` append, `2>` errors, `\|` pipe |
| Safe mode | `set -euo pipefail` |
| File tests | `-f` file, `-d` dir, `-e` exists, `-r` readable |
| Debug | `bash -x script.sh` |
