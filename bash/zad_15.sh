#!/usr/bin/env bash
# @author Jakub Kijek, Informatyka, sem. 1, gr. 2
# @date 2026.10.22

file="zad_15_names.txt"

cat > "$file" << END
Zofia
Adam
Krzysztof
Ewa
Bartek
Marta
END

echo "--- before ---"
cat "$file"

echo "--- after sort ---"
sort "$file"
