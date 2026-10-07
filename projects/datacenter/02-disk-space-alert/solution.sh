#!/usr/bin/env bash
awk 'NR>1 && +$5>=80 {print "ALERT", $6, $5}' df.txt
