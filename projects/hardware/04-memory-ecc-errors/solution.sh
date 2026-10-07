#!/usr/bin/env bash
sed 's/ce=//; s/ue=//' edac.txt | awk '$3>0 || $2>100 {print "REPLACE", $1}'
