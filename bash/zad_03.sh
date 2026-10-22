#!/usr/bin/env bash
# @author Jakub Kijek, Informatyka, sem. 1, gr. 2
# @date 2026.10.22

echo "--- last 20 commands from history ---"
tail -n 20 ~/.bash_history

echo
echo "--- clipboard ---"
if command -v wl-paste > /dev/null; then
    wl-paste
elif command -v xclip > /dev/null; then
    xclip -o -selection clipboard
else
    echo "no clipboard tool (wl-paste / xclip) found"
fi
