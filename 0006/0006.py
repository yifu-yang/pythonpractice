# -*- coding : utf-8 -*-
import os 
import sys
import re
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

def readfile(filename=''):
    f=open(filename,'r+',encoding='utf-8')
    txt=f.read()
    f.close()
    return txt

def getkeyword(txt=''):
    if txt=='':
        return 0
    else:
        words=re.split(r'[.,"\s]+',txt)
        keys=buildlist(words)
        
        return findkey(keys)

		
def buildlist(words):
    d=dict()
    for word in words:
        if word in ['I','am','you','they','is','and','the','of','in','on','not','at','to','a','from','for']:
            continue
        if word in d:
            d[word]=d[word]+1
        else:
            d[word]=0
    return d
	
def findkey(d):
    tmp=sorted(d.items(),key=lambda d:d[1])
    return tmp[len(tmp)-1][0]
	
if __name__ == "__main__":
    path=os.path.join(os.getcwd(),sys.argv[1])
    l=getfiles(os.path.join(os.getcwd(),sys.argv[1]))
    print(l)
    for item in l:
        print(getkeyword(readfile(os.path.join(path,item))))