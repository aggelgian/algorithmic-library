#!/bin/sh

DIRS="graphs"

for d in $DIRS
do
  for f in "$d"/*.py
  do
    echo "Running $f ..."
    python3 "$f"
  done
done
