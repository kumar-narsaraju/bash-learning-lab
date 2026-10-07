#!/usr/bin/env bash
read -r n
if (( n % 2 == 0 )); then
  echo "$n is even"
else
  echo "$n is odd"
fi
