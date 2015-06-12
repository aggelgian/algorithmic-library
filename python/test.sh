#!/bin/sh

DIRS="graphs data_structures"

for d in $DIRS
do
  for f in "$d"/*.py
  do
    echo "Running $f ..."
    python3 "$f"
  done
done
