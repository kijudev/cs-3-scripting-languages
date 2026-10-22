#!/usr/bin/env bash
# @author Jakub Kijek, Informatyka, sem. 1, gr. 2
# @date 2026.10.22

output="zad_12_output.txt"

find / -type f -perm -u+x 2>/dev/null > "$output"

echo "list saved to $output"
echo "number of executable files: $(wc -l < "$output")"
