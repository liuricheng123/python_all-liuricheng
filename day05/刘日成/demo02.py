shop=[
    ["iphone",6000],
    ["mac computer",12000],
    ["mi watch",500],
    ["lenovo pc",4500],
]
print("欢迎进入商城".center(70,"-"))
while True:
    salary=input("请输入您的初始金钱：")
    if salary.isdigit():
        salary=  int(salary)
        print("您的初始金钱为：",salary,"，祝您本次购物愉快！")
        break
    else:
        print("请重新输入初始金钱！")
'''
for index,value in enumerate(shop):
    print(index,"-----",value)
'''
mycart=[]
while True:
    for index,value in enumerate(shop):
        print(index,"    ",value)
    choice=input("请输入您要买的商品编号：")
    if choice.isdigit():
        choice=int(choice)
        if choice<len(shop):
            if salary>=shop[choice][1]:
                mycart.append(shop[choice])
                salary-=shop[choice][1]
                print("恭喜你，添加成功！您的余额还剩：",salary)
            else:
                print("对不起，您的余额不足，请充值！")
        else:
            print("对不起，您输入的商品不存在！")
    elif choice=="q" or choice=="Q":
        print("欢迎下次光临")
        break
    else:
        print("输入不合法，请重新输入")
print("-----------------------")
for i in mycart:
    print(i)
print("您的余额为：",salary)