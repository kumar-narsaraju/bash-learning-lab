#!/usr/bin/env bash
grep 'Failed password' auth.log | awk '{for(i=1;i<=NF;i++) if($i=="from") print $(i+1)}' | sort | uniq -c | sort -rn | awk '{print $1, $2}'
