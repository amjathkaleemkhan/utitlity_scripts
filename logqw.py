#!/usr/bin/env python

import sys
import os


dict_1= ['ERROR','error','Error','FAILED','failed','exception','EXCEPTION','java.io.IOException','null','NULL','java.lang.NullPointerException']


def search_str(file_path, word):
    with open(file_path, encoding='latin-1') as file:
        # read all content of a file
        content = file.read()
        # check if string present in a file
        if word in content:
            print('Exist in a file',word,file_path)
#pd.read_csv('File_name.csv',encoding='latin-1')


tot_log_file="for i in `find / -name '*.log' `; do echo $i ;done >tot_log_file.txt"
os.system(tot_log_file)

with open('tot_log_file.txt', encoding='latin-1') as p1:
        c1 = p1.readlines()
        for file in c1:
           r=file.strip()
           for d in dict_1:
              search_str(r, d)

#os.system('rm -rf tot_log_file.txt')
print("Exiting now")
