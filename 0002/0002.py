# coding = utf-8
import random
import pymysql

def create(randomlength):
    chars='AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    s=''
    for i in range(randomlength):
        s+=chars[random.randint(0, len(chars)-1)]
    return s
	
def InsertToDb(code):
    conn=pymysql.connect(user='root',password='1qazZAQ!',host='localhost',database='python')
    sqlstr="Insert into python.ooo2(code) values ('"+code+" ')"
    print(sqlstr)
    cursor=conn.cursor()
    try:
        cursor.execute(sqlstr)
    except Exception as err:
        print(err)
    finally:
        conn.commit()
        cursor.close()
        conn.close()
	
if __name__ =='__main__':
    for x in range(200):
	    code=create(8)
	    InsertToDb(code)