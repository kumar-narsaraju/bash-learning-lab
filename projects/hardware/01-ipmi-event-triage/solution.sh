#!/usr/bin/env bash
grep -E 'Critical|Uncorrectable' sel.txt
n=$(grep -cE 'Critical|Uncorrectable' sel.txt)
echo "Critical events: $n"
