#!/usr/bin/env python3
#问题：
# 1.无法识别目录下的目录
# 2.无法识别文件格式
import os
import shutil


files_Number = 0
folder_Number = 0
files_per_folder = 300
b = 0
#path = os.getcwd()
path = input("请输入筛选路径:\n")
print("开始整理文件，请勿关闭终端")
file_lists = []
#filelists = os.listdir(path)
#print (path)
#print(filelists)
#获取当前目录所有文件数量
for root, dirs, files in os.walk(path):
    for file in files:
        files_Number += 1
        file_lists.append(file)

print ("共有"+str(files_Number)+"个文件") 
#print (len(file_lists))
#print (file_lists)
#根据文件数量创建文件夹
if files_Number < files_per_folder:
    folder_Number = 1
    folder_path = path +"\\100Photo"
    os.mkdir(folder_path)
    for file in file_lists:
            #print(path + "\\"+ file)
            shutil.move(path + "\\"+ file, folder_path)  
elif files_Number > files_per_folder:
    folder_Number = int(files_Number/files_per_folder) + 1
    print ("需要创建"+str(folder_Number)+"个文件夹")
    while folder_Number > 0:
        a = str(100 + b)
        folder_path = path +"\\"+ a + "Photo"
        os.mkdir(folder_path)
        folder_Number -= 1
        b += 1
        if files_per_folder-len(file_lists)<=0:
            n = 0
            while n < files_per_folder:
                if len(file_lists)>n:
                    #print (n,len(file_lists))
                    filePop = file_lists.pop(n)
                    #print(path + "\\"+ filePop)
                    shutil.move(path + "\\"+ filePop, folder_path)
                    n += 1
                else:
                    m = files_per_folder - n
                    filePop = file_lists.pop(m)
                    #print(path + "\\"+ filePop)
                    shutil.move(path + "\\"+ filePop, folder_path)
                    n += 1
        else:
            while len(file_lists) > 0: 
                y = len(file_lists)-1
                print(y,len(file_lists))
                if y >= 0:
                    filePop = file_lists.pop(y)
                    shutil.move(path + "\\"+ filePop, folder_path)
                    y -= 1
                else:
                    print(y)
                    break

print("整理结束")
#将文件名存入数组
#创建目录目录名100Photo
#每个目录放300个文件
