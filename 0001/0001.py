# coding = utf-8
import random
def create(randomlength):
    chars='AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    s=''
    for i in range(randomlength):
        s+=chars[random.randint(0, len(chars)-1)]
    return s
def writefile():
    f=open("result.txt",'a')
    #print (create(8))
    s=create(8)
    f.write(s)
    f.write('\n')
    f.close()
if __name__ == '__main__':
    for x in range(0,200):
        writefile()