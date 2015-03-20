# coding = utf-8
import random
import redis

def create(randomlength):
    chars='AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    s=''
    for i in range(randomlength):
        s+=chars[random.randint(0, len(chars)-1)]
    return s
	
def InsertToRedis(code):
    r=redis.Redis(host='localhost',port='6379',db=0)
    r.set(code,code)
	
	
def getInfo():
    r=redis.Redis(host='localhost',port='6379',db=0)
    #r.flushdb()
    print(r.dbsize())
    #r.save()
	
if __name__=='__main__':
    for x in range(200):
	    str=create(8)
	    InsertToRedis(str)
    getInfo()