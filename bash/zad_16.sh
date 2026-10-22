#!/usr/bin/env bash
# @author Jakub Kijek, Informatyka, sem. 1, gr. 2
# @date 2026.10.22

port=12345

if [ -z "$1" ]; then
    echo "waiting on port $port..."
    nc -l "$port"
else
    echo "connecting to $1:$port..."
    nc "$1" "$port"
fi
