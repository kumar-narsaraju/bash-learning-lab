# Bash Learning Lab

Learn **Linux bash scripting** from zero by writing real scripts. Free, hands-on, with automatic checking.


## Learn online (no install)
- **Lessons and quizzes:** open the website at `https://<your-username>.github.io/bash-learning-lab/` (GitHub Pages).
- **Bash terminal and code editors inside the website itself:** nothing to install and no sign-in. Type commands in the terminal on the home page, or write `answer.sh` in a lesson and press **Check answer**. (Powered by the open-source `just-bash` simulator in `docs/vendor/`, Apache-2.0.)
- **Full-page terminal:** open `terminal.html` on the site (link in the left menu). It has sample data-center and server-hardware files; type `help-lab`.
- **Full real Linux (optional):** click **Code → Codespaces → Create codespace** for a complete terminal; then run `./check.sh 01`.

## Quick start (on your own computer)
```bash
git clone https://github.com/<your-username>/bash-learning-lab.git
cd bash-learning-lab
chmod +x check.sh check-all.sh
cat modules/01-first-script/lesson.md       # read the lesson
nano modules/01-first-script/answer.sh      # write your answer
./check.sh 01                               # PASS or FAIL with a diff
```
Works on any Linux, macOS, or Windows with WSL. No installs needed except bash.

## The path
| # | Module |
|---|---|
| 01 | [Your First Script](modules/01-first-script/lesson.md) |
| 02 | [Variables and Input](modules/02-variables-input/lesson.md) |
| 03 | [Making Decisions (if)](modules/03-conditionals/lesson.md) |
| 04 | [Loops](modules/04-loops/lesson.md) |
| 05 | [Functions and Arguments](modules/05-functions-arguments/lesson.md) |
| 06 | [Working with Text](modules/06-text-processing/lesson.md) |
| 07 | [case and Arrays](modules/07-case-arrays/lesson.md) |
| 08 | [Safe Scripts and Error Handling](modules/08-error-handling/lesson.md) |
| 09 | [Logging and Automation](modules/09-logging-automation/lesson.md) |
| 10 | [Mini Project: Word Report](modules/10-mini-project/lesson.md) |

Then do the career projects: [Data Center SysAdmin](projects/datacenter/README.md) and [Server Hardware Troubleshooting](projects/hardware/README.md) (check with `./check.sh datacenter/01-rack-inventory`), build your own tools in [`projects/`](projects/README.md), keep the [`cheatsheet.md`](cheatsheet.md) open, and start every real script from [`templates/script-template.sh`](templates/script-template.sh).

## Training sessions
A ready-made 4-week plan for groups and self-study: [SESSIONS.md](SESSIONS.md).

## How to learn well
1. Type the code; never paste.
2. Break it on purpose, then fix it.
3. Debug with `bash -x script.sh` and `shellcheck script.sh` (free linter).
4. Read the error message slowly; it usually names the line.
5. Automate something real in your own life.

## Contributing
Add lessons, exercises, or projects. See [CONTRIBUTING.md](CONTRIBUTING.md). MIT licensed.
