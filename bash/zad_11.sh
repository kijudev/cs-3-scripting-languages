#!/usr/bin/env bash
# @author Jakub Kijek, Informatyka, sem. 1, gr. 2
# @date 2026.10.22

echo "computer name: $(hostname)"

echo
echo "---- volumes ----"
lsblk -o NAME,SIZE,TYPE,MOUNTPOINT
echo "number of volumes: $(lsblk -n -o NAME | wc -l)"

echo
echo "---- network cards ----"
count=0
for card in /sys/class/net/*; do
    name=$(basename "$card")
    mac=$(cat "$card/address")
    echo "$name: $mac"
    count=$((count + 1))
done
echo "number of network cards: $count"

echo
echo "---- addressing ----"
echo "domain: $(hostname -d)"
ip -brief address
