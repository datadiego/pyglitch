#!/bin/bash

#for loop 0 to 255

for i in $(seq 1 255); do
# replace for random values
    python find_and_replace.py hack.bmp hack.bmp $i $((RANDOM%255))
done