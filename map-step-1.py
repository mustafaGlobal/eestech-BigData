#!/usr/bin/python
import sys
import os


for line in sys.stdin:
    if(line.find('Tags=') != -1):

        tag_index =  line.find('Tags=')
        answer_index = line.find('AnswerCount')
        line = line[tag_index + 6:answer_index-2]

        line=line.replace("&lt;" , "$")
        line=line.replace("&gt;" , "$")

        data = line.strip().split('$')
        prazno_mjesto = data[0]

        for i in range(0,len(data)):
            if data[i] == prazno_mjesto :
                continue
            print data[i], "\t", 1







