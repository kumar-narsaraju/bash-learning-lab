#!/usr/bin/env bash
awk '$2>90 {print "REBOOT", $1, "(" $2 " days)"; n++} END {print "Total:", n+0}' servers.txt
