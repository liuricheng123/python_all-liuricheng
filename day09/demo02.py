import pymysql

con=pymysql.connect(host="localhost",user="root",password="",database="学生数据库",charset="utf8")
cursor=con.cursor()
sql="insert into student values ('s6','张辉','女',22,3)"
s=cursor.execute(sql)
print(s)
con.commit()
cursor.close()
con.close()