#!/bin/bash

# Find all latex files in subdirectories
for file in $(find . -name "*.tex" -type f)
do
  # Compile the latex file to pdf
  pdflatex "$file"
done
