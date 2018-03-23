#!/usr/bin/python

import sys

numberTotal = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")

    if len(data_mapped) != 2:
        continue

    thisKey, thisNumber = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", numberTotal
        oldKey = thisKey;
        numberTotal = 0

    oldKey = thisKey
    numberTotal += float(thisNumber)

if oldKey != None:
    print oldKey, "\t", numberTotal
