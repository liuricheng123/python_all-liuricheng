# import xlrd
import pymysql
# data=xlrd.open_workbook("E:\\pytho\\xsxl\\b.xlsx")
# sheet=data.sheet_by_name("用户管理")
# print("有",sheet.nrows,"行数据！有",sheet.ncols,"列数据！")
# row=sheet.nrows
# cols=sheet.ncols
# f=open("用户管理器.txt","w+",encoding="utf-8")
# a=[]
# for i in range(row):
#     a=[]
#     for j in range(cols):
#         a.append(str(sheet.cell_value(i,j)).replace(".0",""))
#     string=",".join(a)
#     f.write(string)
#     print(string)

con=pymysql.connect(host="localhost",user="root",password="",database="day10")
cursor=con.cursor()
sql="insert into person values('张三',56,'男','13552648187'),('李四',63,'男','15244851815'),('王五',20,'男','10271515551'),('何登勇',42,'男','15845264556'),('张燕',23,'女','15595226248')"
s=cursor.execute(sql)
con.commit()
cursor.close()
con.close()
