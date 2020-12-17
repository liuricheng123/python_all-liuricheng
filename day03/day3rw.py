'''
#九九乘法表
num = int(input("请输入层数："))
a=1
while a <=num:
    print("第",a,"层",end="")
    b=1
    while b<=a:
        print(b,"x",a,"=",(b*a),"\t",end="")
        b=b+1
    print()
    a=a+1
'''

'''
#九九乘法表倒着，没写对
num = int(input("请输入层数："))
a=1
while a<=num:
    print("第",a,"层",end="")
    b=1
    while b<=a:
        print(b,"x",a,"=",(b*a),"\t",end="")
        b=b+1
    print()
    a=a+1
'''


'''
for a in range(0,9):
    for b in range(0,9-a):
        print("",end="")
'''



'''
输入三次密码错误第一种自己写的
i=2
a=123456
while i<5:
    mima=int(input("请输入密码"))
    if mima!=a:
        print("请重新输入！")
    else:
        print("输入正确")
        break
    i=i+1
'''

'''
三次密码课
name="lrc"
password="123456"
for i in range(3):
    n=input("请输入账户名：")
    p=input("请输入密码：")
    if n==name and p==password:
        print("登陆成功！")
        break
    else :
        print("登陆失败！请重新输入！")
        if i==2:
            print("三次机会用完，账号已冻结！")
            break

'''



'''
青蛙爬井
j=20
s=3
t=2
day=0
pg=0
while True:
    day=day+1
    pg=pg+3
    if pg>=j:
       print("青蛙爬出来用了",day,"天")
       break
    pg=pg-t
'''


'''
A与B调换
A=56
B=78
A=A+B
B=A-B
A=A-B
print(A,B)
'''

'''
三角形判断
a=int(input("请输入第一条边："))
b=int(input("请输入第二条边："))
c=int(input("请输入第三条边："))
if (a+b>c) and (a+c>b) and (b+c>a):
    if (a==b==c):
        print("构成等边三角形！")
    elif (a==b or a==c or b==c):
        print("构成等腰三角形！")
    elif (a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a):
        print("构成直角三角形！")
    else:
        print("构成普通三角形！")
else:
    print("不能构成三角形！")
'''

'''
九九乘法表正着
for i in range(1,10):
    for j in range(1,i+1):
        print(j,"x",i,"=",(i*j),"\t",end="")
    print()
'''

'''
九九乘法表倒着
for i in range(9,0,-1):
    for j in range(1,i+1):
        print(j,"x",i,"=",(i*j),end="\t")
    print()
'''

'''
987654321倒着
for i in range(9,0,-1):
    print(i)
'''

'''
星号排列成三角形
'''
n=int(input("请输入三角形的层数"))
i=1
while i <=n:
    j=1
    while j <=(n-i):
        print(" ",end="")
        j=j+1
    k=1
    while k <= i:
        print ("* ",end="")
        k=k+1
    i=i+1
    print()



