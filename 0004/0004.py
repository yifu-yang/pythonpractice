# -*- coding :utf-8  -*-
import re
import sys
import codecs

def readfile(filename=''):
    f=codecs.open(filename,'r+',encoding='utf-8')
    txt=f.read()
    f.close()
    return txt

def countword(txt=''):
    if txt=='':
        return 0
    else:
        num=len(re.split(r'[.,"\s]+',txt))
        return num

if __name__=="__main__":
    print(countword(readfile(sys.argv[1])))
    print(len(readfile(sys.argv[1]).split()))