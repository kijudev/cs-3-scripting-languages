#!/usr/bin/env bash
# @author Jakub Kijek, Informatyka, sem. 1, gr. 2
# @date 2026.10.22

dir="wczesniej_niz_4_mies"
files=("$dir"/*)

for ((i = 0; i < ${#files[@]}; i++)); do
    for ((j = i + 1; j < ${#files[@]}; j++)); do
        if cmp -s "${files[i]}" "${files[j]}"; then
            echo "${files[i]} == ${files[j]}"
        else
            echo "${files[i]} != ${files[j]}"
        fi
    done
done
