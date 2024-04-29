#!/bin/bash

# Improved header (assuming Python 3)
header="#!/usr/bin/env python3"

# Iterate over files listed by `ls -l` (excluding total lines)
for file in $(ls -l *.py | tail -n +2); do
  # Check if the file is a regular file (avoid modifying directories)
  if [[ -f "$file" ]]; then
    # Prepend the header only to regular files
    echo "$header" > "$file"
  fi
  # Always echo the filename for reference
  echo "$file"
done
