#!/usr/bin/env bash
# Name:        my-script.sh
# Description: What this script does
# Usage:       ./my-script.sh <argument>
set -euo pipefail

usage() { echo "Usage: $0 <argument>" >&2; exit 1; }
log()   { echo "[$(date '+%F %T')] $*"; }

main() {
  [[ $# -ge 1 ]] || usage
  log "Starting with: $1"
  # your code here
  log "Done"
}
main "$@"
