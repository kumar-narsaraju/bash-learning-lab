#!/usr/bin/env bash
for d in modules/*/; do n=$(basename "$d"); n=${n%%-*}; ./check.sh "$n" "$@" || exit 1; done
for p in projects/*/*/; do [[ -f $p/expected.txt ]] || continue; ./check.sh "${p#projects/}" "$@" || exit 1; done
