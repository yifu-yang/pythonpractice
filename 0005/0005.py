# -*- coding :utf-8 -*-
from PIL import Image
import os
import sys

width=640
height=1136

path=''
def getfiles(dir=''):
    files= []
    if not os.path.exists(dir):
        return files
    for x in os.listdir(dir):
        #print(x)
        if not os.path.isdir(x):
            files.append(x)
            #print(len(files))
    return files
	
def changesize(filename=''):
    #print(filename)
    if filename=='':
        return 0
    p=Image.open(filename)
    #print(p.size)
    if p.size[0]>p.size[1]:
        p=p.resize((height,width))
    else:
        p=p.resize((width,height))
    p.save(filename+'.jpg')

if __name__ == '__main__':
    path=os.path.join(os.getcwd(),r'1')
    l=getfiles(os.path.join(os.getcwd(),r'1'))
    for item in l:
        changesize(os.path.join(path,item))