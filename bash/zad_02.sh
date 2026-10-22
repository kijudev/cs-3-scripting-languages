#!/usr/bin/env bash
# @author Jakub Kijek, Informatyka, sem. 1, gr. 2
# @date 2026.10.22

dir=${1:-/}

find "$dir" -maxdepth 2 -type d 2>/dev/null | sort
