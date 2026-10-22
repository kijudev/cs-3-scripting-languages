#!/usr/bin/env bash
# @author Jakub Kijek, Informatyka, sem. 1, gr. 2
# @date 2026.10.22

dir="wczesniej_niz_4_mies"

for file in "$dir"/*; do
    echo "=== $file ==="
    less "$file"
done
