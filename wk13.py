#!/usr/bin/env python3.7

#generate list of dictioniaries about files in your current working directory

import os

#get current working directory
directory = os.getcwd()

#create empty list

files = []
#search through files in current working directory

for file_name in os.listdir(directory):
    
#get file path
    file_path = os.path.join(directory, file_name)
    
    #get file size
    file_size = os.path.getsize(file_path)
    
    #create dictionary
    
    file_info = {
        'file_name': file_name,
        'file_path': file_path,
        'file_size': file_size,
    }
#add file info to empty list

    files.append(file_info)
    
#print list of dictionaries

    print(file_info, sep="\n")
    
    

  
    



