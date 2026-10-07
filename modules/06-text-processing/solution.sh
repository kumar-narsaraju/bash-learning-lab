#!/usr/bin/env bash
awk -F, '{ s += $2 } END { print "Total: " s }'
