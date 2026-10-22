#!/usr/bin/env bash
# @author Jakub Kijek, Informatyka, sem. 1, gr. 2
# @date 2026.10.22

cd ~ || exit 1
ls

read -p "first file: " file1
read -p "second file: " file2

if diff "$file1" "$file2"; then
    echo "files are the same"
fi
