#!/usr/bin/env bash
# @author Jakub Kijek, Informatyka, sem. 1, gr. 2
# @date 2026.10.22

output="zad_17_output.txt"

find ~ -type f -name "*.txt" ! -name "$output" -exec cat {} + > "$output"

echo "saved to $output ($(wc -l < "$output") lines)"
