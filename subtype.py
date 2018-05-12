#!/usr/bin/env python
# -*- coding: utf-8 -*-
__metaclass__ = type


import re
file1 = open("sample_subtype","r")
#count = len(fr_raw_data.readlines())
#print(count)
file2 = open("merged.without_SNP.without_NA.head","r")
file3 = open("output","w")

sample_lines = file1.next().strip().split("\t")
sample_store_list=[]


for each_col in sample_lines:
    sample_store_list.append(each_col)
    
    
for i in sample_store_list:
    for line in file2.next().strip():
        match = re.search(i,line)
        if match:
            file3.write(line)

file1.close()
file2.close()
file3.close()
    
