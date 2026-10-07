#!/usr/bin/env bash
read -r cmd
case "$cmd" in
  start) echo "Starting service" ;;
  stop)  echo "Stopping service" ;;
  *)     echo "Unknown command" ;;
esac
