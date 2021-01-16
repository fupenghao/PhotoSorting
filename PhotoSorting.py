#!/usr/bin/env python3
#Issues：
# 1.Can not check if a folder already exits.
# 2.Can not classify types of files.

import os
import shutil
path = "C:\\Users\\fupen\\Pictures\\Library\\建筑"
#path = input("Pls type in the Working Directory:\n")
files_number = 0
folder_Number = 0
files_per_folder = 300
file_lists = []
folder_lists = []
Exist_folder_lists = []
folder_suffix = "Photo"
folder_path = ""

def printLine():
    print(140 * "=")

# Calcute the pic numbers and put their pwd in a list

def getList():
    global files_number
    global file_lists
    global Exist_folder_lists
    for root, dirs, files in os.walk(path):
        #for file in files:
            # Get the file numbers
        # files_number += 1
        # file_lists.append(file)
        for name in files:
            file = os.path.join(root, name)
            #print(os.path.join(root, name))
            if os.path.isfile(file):
                file_lists.append(file)
            else:
                Exist_folder_lists.append(file)
        for name in dirs:
            file = os.path.join(root, name)
            #print(os.path.join(root, name))
            if os.path.isfile(file):
                file_lists.append(file)
            else:
                Exist_folder_lists.append(file)
        #print (root)
        #print (dirs)
    files_number=len(file_lists)
    printLine()
    print ("There are " + str(files_number) + " files.")
# Gengerate folder lists and test if there is any repetition
def calFolders():
    global folder_Number
    global Exist_folder_lists
    #print (files_number)
    #print (len(file_lists))
    if files_number < files_per_folder:
        folder_Number = 1
        print ("Only 1 folder will be generated")
    elif files_number > files_per_folder:
        folder_Number = int(files_number/files_per_folder) + 1
        print (str(folder_Number)+" folders will be created")
# Generate Folder Names
def genFolderName():
    global folder_lists
    x = folder_Number  
    if x == 1:
        folder_path = "\\100" + folder_suffix
        folder_lists.append(folder_path)
    if x > 1:
        a = 100
        while x > 0:         
            folder_path = "\\" + str(a) + folder_suffix
            folder_lists.append(folder_path)
            a += 1
            x -= 1

# Generate Folders
def makeFolders():
    for folders in folder_lists:
        os.mkdir(path + folders)

# Put Pictures into the Folders
def moveFiles():
    print ("Moving Started.")
    if files_number < 300:
        for files in file_lists:
            shutil.move(files, path + str(folder_lists[0]))
    else:
        x = folder_Number
        print (x)
        while x > 0:
            n = files_per_folder
            print (n)
            while n > 0:
                b = len(file_lists)
                if b > n: 
                    #print (n,b)
                    targetPath = path + str(folder_lists[x-1])
                    #print (targetPath)
                    shutil.move(file_lists.pop(n-1), targetPath)
                    n -= 1
                else:
                    print (b)
                    if b > 0:
                        while b > 0:
                            targetPath = path + str(folder_lists[x-1])
                            #print (targetPath)
                            shutil.move(file_lists.pop(b-1), targetPath) 
                            b -= 1
                    else:
                        print("Sort Finished")
                        break
            x -= 1

def Monitor():
    printLine()
    #print("This is file lists")
    #print (file_lists)
    #printLine()
    #print("This is file folder lists")
    #print (Exist_folder_lists)
    print("These folders will be created")
    print (folder_lists)
    printLine()

def main():
    getList()
    calFolders()
    genFolderName()
    makeFolders()
    moveFiles()
    Monitor()

main()