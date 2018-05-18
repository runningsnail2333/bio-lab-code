import sys
import os
fr_file = (sys.argv[1],"r")
file_name_input = os.path.basename(sys.argv[1])
fw_file = file(file_name_input + ".t","w")


target = True

list_t=[]

for line in fr_file:
    line_list =line.strip().split("\t")
    
    if target:
        n_col = len(line_list)
        for i in range(n_col):
            list_t.append([])
        target = False
    i = 0

    for col_one in line_list:
        list_t[i].append(col_one)
        i = i +1

for one_row_to_write in list_t:
    fw_file.write("\t".join(one_row_to_write)+"\n")


