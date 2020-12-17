name=input("请输入姓名：")
sex=input("请输入性别：")
age=input("请输入年龄：")
id=input("请输入身份证号：")
high=input("请输入身高：")
weight=input("请输入体重：")

info='''
---------------个人信息----------------
姓名：{name}
性别: {sex}
年龄：{age}
身份证号：{id}
身高：{high}
体重：{weight}
--------------------------------------
'''
print(info.format(name=name,sex=sex,age=age,id=id,high=high,weight=weight))

