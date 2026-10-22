#!/usr/bin/env bash
# @author Jakub Kijek, Informatyka, sem. 1, gr. 2
# @date 2026.10.22

echo "all processes: $(ps -e --no-headers | wc -l)"
echo "processes of $USER: $(ps -u "$USER" --no-headers | wc -l)"
