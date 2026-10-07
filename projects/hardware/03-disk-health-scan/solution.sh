#!/usr/bin/env bash
awk '{ if ($2>0 || $3>0) print "FAILING", $1, "(realloc=" $2 " pending=" $3 ")"; else h++ } END {print "Healthy disks:", h+0}' smart.txt
