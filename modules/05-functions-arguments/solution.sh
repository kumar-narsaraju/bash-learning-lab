#!/usr/bin/env bash
add() {
  echo $(( $1 + $2 ))
}
echo "Sum: $(add "$1" "$2")"
