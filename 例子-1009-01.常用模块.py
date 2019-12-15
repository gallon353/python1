#coding=utf-8
#os模块
'''
import os
os.system('dir')         #运行系统中的命令dir
#os.remove('D:\\tel.txt')#删除系统中的文件
print(os.getcwd())       #当前目录的绝对路径
print(os.listdir('D:\\'))      #指定目录下所有文件
print(os.path.split('D:\\soft\\test.txt'))#返回一个路径的目录和文件名
print(os.path.isfile('D:\\soft\\test.txt'))#判断是否是文件
#os.path.isdir()  判断是否是目录
#os.path.exists() 判断是否存在
'''
#sys模块
import sys
print(sys.version)

print(sys.path)
