#!/usr/bin/env bash
awk -F' \\| ' '$4!="ok" {print "CHECK " $1 ": " $2 " " $3}' sensors.txt
