import pymysql

con=pymysql.connect(host="localhost",user="root",password="",database="lttest",charset="utf8")
cursor=con.cursor()
sql="insert into person values('张三',46,200,'男')"
s=cursor.execute(sql)
print(s)
con.commit()
cursor.close()
con.close()