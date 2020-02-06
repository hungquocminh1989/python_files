#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#-----------------------------------------------------------------------------
# Name:        Script phân loại file theo định dạng và dung lượng
#
# Purpose:
#
# Version:     1.1
#
# Author:
#
# Created:     06/02/2020
# Updated:     06/02/2020
#
# Copyright:   -
#
#-----------------------------------------------------------------------------
"""

#Import lib
import os, re, fnmatch, shutil
from datetime import datetime

class AnalyzeFolder:

    def __init__(self, input_folder, output_folder, pattern, size_group):
        self.input_folder = os.path.normpath(input_folder)
        self.output_folder = os.path.normpath(output_folder)
        self.pattern = pattern
        self.size_group = size_group
        self.size_group.sort()
        print(self.size_group)

        if not os.path.exists(self.input_folder):
            print(self.input_folder)
            print("Folder input not exists")
            exit()

        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

    #Check size file and create folder
    def get_file_size(self, file_path):
        return os.path.getsize(file_path)

    #Get list file
    def get_list_file(self, target_files, nontarget_files):
        try:
            for path, subdirs, files in os.walk(self.input_folder):
                for name in files:
                    file_path = os.path.join(path, name)
                    if re.search(self.pattern, name):
                        size_byte = self.get_file_size(file_path)
                        size_mb = size_byte/1024/1024 #Convert Byte to Megabyte
                        target_files[file_path] = size_mb
                    else:
                        nontarget_files[file_path] = "-"
            return True
        except:
            return False

    def create_and_copy_file(self, dicFile):
        for file, size in dicFile.items():
            iter_size_group = iter(self.size_group)
            next(iter_size_group)
            for limit in size_group:
                limit_end = next(iter_size_group, "")
                #print("-- {0} ~ {1}".format(limit, limit_end))
                if size >= limit and (limit_end == "" or size <= limit_end):

                    org_file_name = os.path.basename(file)
                    filename, file_extension = os.path.splitext(org_file_name)
                    
                    #Create folder storage
                    folder_name = "Size {0}MB ~ {1}MB".format(limit, limit_end)
                    if limit_end == "":
                          folder_name = "Size {0}MB ~".format(limit)  
                    folder_path = os.path.join(self.output_folder, folder_name)
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)

                    #Create folder extension
                    if file_extension == "":
                        file_extension = "non_extension_files"
                    folder_path = os.path.join(folder_path, file_extension)
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)

                    #Copy file
                    random_file_name = "File_" + datetime.now().strftime('%Y%m%d%H%M%S%f')+ "_(Duplicate with {0})".format(org_file_name) + file_extension
                    file_dist_random_path = os.path.join(folder_path, random_file_name)
                    file_dist_org_path = os.path.join(folder_path, org_file_name)
                    if os.path.exists(file):
                        if not os.path.exists(file_dist_org_path):
                            shutil.copyfile(file, file_dist_org_path)
                            print("Created file {0}".format(file_dist_org_path))
                        else:
                            shutil.copyfile(file, file_dist_random_path)
                            print("Created file {0}".format(file_dist_random_path))
                    break
        
    def analyze(self):
        target_files = {}
        nontarget_files = {}
        result_get_list = self.get_list_file(target_files, nontarget_files)

        if result_get_list == True:
            #print(target_files)
            #print(nontarget_files)
            self.create_and_copy_file(target_files)
        else:
            print("Có lỗi xảy ra.")

#Start application
size_group = [0, 10, 20] #MB
test = AnalyzeFolder("D:\\SVN_PC_08\\MMEN\\01.Docs\\99_Temp", "C:\\py_output", "^.*.*$", size_group)
test.analyze()
exit()
