#!/usr/bin/python
import sys
import os


def nadji_broj_ponavljanja(nStr ,pattern):
    count = 0
    flag = True
    start = 0
    while flag:
        a = nStr.find(pattern, start)  # find() returns -1 if the word is not found,
        # start i the starting index from the search starts(default value is 0)
        if a == -1:  # if pattern not found set flag to False
            flag = False
        else:  # if word is found increase count and set starting index to a+1
            count += 1
            start = a + 1
    return count



broj_ponavljanja = 0
broj_linija = 90



from itertools import islice
with open("rezultat_faze_1") as myfile:
    head = list(islice(myfile, broj_linija))

listica = [None] * broj_linija

i=0

for line in head:
    data = line.strip().split("\t");
    listica[i] = data[0]
    i=i+1


for line_xml in sys.stdin:
    body_index = line_xml.find('Body=')
    owner_index = line_xml.find('OwnerUserId')
    if (body_index == -1) or (owner_index == -1):
        continue
    line_xml = line_xml[body_index:owner_index]

    for lst in listica:
        if line_xml.find(lst) != -1 :
            broj = nadji_broj_ponavljanja(line_xml,lst)
            print lst, "\t", broj















