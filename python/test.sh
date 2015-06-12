#!/bin/sh

DIRS="graphs data_structures"

# Add the python files to python's paths.
for d in $DIRS
do
  export PYTHONPATH=$PYTHONPATH:"$d"
done

# Run the tests.
for d in $DIRS
do
  for f in "$d"/*.py
  do
    echo "Running $f ..."
    python3 "$f"
  done
done
