# Failed SSH login hunter

**Goal:** `auth.log` is a login log. Print the source IPs of `Failed password` lines with their counts, most attempts first, as `<count> <ip>`.

**Hint:** `grep 'Failed password'`, then pull the IP (the word after `from`), then `sort | uniq -c | sort -rn`.

Sample data: `auth.log`. Write `answer.sh` in this folder and check it with `./check.sh datacenter/03-failed-ssh-logins`.
