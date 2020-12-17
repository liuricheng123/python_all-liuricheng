db={}
#开始读取db.txt文件
f=open("db.txt","r+",encoding="utf-8")
data=f.readlines()#["张三“，”root"]
for i in data:
    line=i.split(":")#通过：将前后进行分W割
    db[line[0]]=line[1].replace("\n","")#将\n改为空值
#注册模块
while True:
    name=input("请输入用户名：")
    password=input("请输入密码：")
    if len(name) != 0 and len(password) != 0:
        if name in db:
           print("该用户已存在！")
        else:
           db[name]=password
        break
    else:
      print ("输入不能为空")


w=open("db.txt","w+",encoding="utf-8")
for key in db:
    w.write("{name}:{password}\n".format(name=key,password=db[key]))
w.close



#登录模块
# if name in db:
#     if password==db[name]:
#         print("登陆成功！")
#     else:
#         print("密码输入错误！")
# else:
#     print("该用户不存在！")


