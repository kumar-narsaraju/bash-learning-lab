#!/usr/bin/env bash
count=0
longest=""
while read -r w; do
  count=$((count + 1))
  if (( ${#w} > ${#longest} )); then longest="$w"; fi
done
echo "Count: $count"
echo "Longest: $longest"
