#!/usr/bin/env bash
# @author Jakub Kijek, Informatyka, sem. 1, gr. 2
# @date 2026.10.22

src=${1:-$HOME}
dest="wczesniej_niz_4_mies"

mkdir -p "$dest"
find "$src" -maxdepth 1 -type f -mtime +120 -exec cp {} "$dest" \;

echo "copied files:"
ls "$dest"
