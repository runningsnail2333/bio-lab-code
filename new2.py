'''

# -*- coding: utf-8 -*-
__metaclass__ = type
# Author: Li Guochao

import re
import sys
import random
import string
INFILE = open("merged.without_SNP.without_NA_head1000","r")
#INFILE = open("/share_bio/unisvx1/sunyl_group/ligch/Database/TCGA/breast_cancer/breast_cancer/merged.without_SNP.without_NA.head1000", "r")
outfile = open ("y","w")
regex = re.compile(r"TCGA-A7-A26E-01A|TCGA-A7-A26J-01A|TCGA-E2-A1AZ-")

first_cycle = True
sample_list = []
b=INFILE.readlines()


for x in INFILE:
    a = b.strip().split("\t")
    ret = re.split(regex,a)
    outfile.write(ret)

''' #想法不成熟，借鉴了师兄的代码想法



#!/usr/bin/env python
# -*- coding: utf-8 -*-
__metaclass__ = type

r_raw_data = read("merged.without_SNP.without_NA","r")
duplicated_list = ["TCGA-A7-A26E-01A","TCGA-A7-A26J-01A"]

sample_need_list =[]
sample_index_list=[]
head_line_raw_data = fw_raw_Data.next().strip().split("\t")
for one_col in head_line_raw_data:
    if one_col not in duplicated_list:
        sample_need_list.append(one_col)#没有匹配duplication list的行的信息记录下来
        sample_index_list.append(head_line_rawdata_list.index(one_col))#把每一行对应的索引记录下来，然后进行记录，以便后续的for循环
out_file = file("merged.without_SNP.without_NA.remove_duplicate_col","w")
out_file.write("\t".join(sample_need_list)+"\n")
for line in fr_raw_data:
    line_list = line.strip(),split("\t")
    line_to_write =[]
    for one_index_write in sample_index_list:
        line_to_write.append(line_list[one_index_write])
    fw.file.write("\t".join(line_to _write)+ '\n')

fr_raw_data.close()
out_file.close()
        


    
        
