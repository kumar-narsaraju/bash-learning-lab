#!/usr/bin/env bash
read -r f
if [[ ! -f "$f" ]]; then
  echo "Error: file not found"
  exit 1
fi
echo "OK"
