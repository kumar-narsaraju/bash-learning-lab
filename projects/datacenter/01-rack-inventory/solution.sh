#!/usr/bin/env bash
tail -n +2 inventory.csv | cut -d, -f2 | sort | uniq -c | awk '{print $2": "$1}'
echo "NOT ONLINE:"
tail -n +2 inventory.csv | awk -F, '$5!="online"{print $1}'
