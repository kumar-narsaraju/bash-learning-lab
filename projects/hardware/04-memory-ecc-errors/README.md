# Memory ECC error finder

**Goal:** `edac.txt` lines look like `DIMM_A1 ce=0 ue=0` (correctable and uncorrectable errors). Replace a DIMM when ue>0 or ce>100. Print `REPLACE <dimm>` for those, one per line.

**Hint:** Remove the `ce=`/`ue=` text with `sed` or use awk `split($2,a,"=")`.

Sample data: `edac.txt`. Write `answer.sh` in this folder and check it with `./check.sh hardware/04-memory-ecc-errors`.
