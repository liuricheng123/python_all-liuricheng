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