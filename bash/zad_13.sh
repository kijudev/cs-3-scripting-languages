#!/usr/bin/env bash
# @author Jakub Kijek, Informatyka, sem. 1, gr. 2
# @date 2026.10.22

host=${1:-8.8.8.8}

if ping -c 4 "$host"; then
    echo "connection OK"
else
    echo "no connection to $host"
fi
