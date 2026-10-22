#!/usr/bin/env bash
# @author Jakub Kijek, Informatyka, sem. 1, gr. 2
# @date 2026.10.22

echo "---- disks and partitions ----"
lsblk

echo
echo "---- usage of mounted filesystems ----"
df -h
