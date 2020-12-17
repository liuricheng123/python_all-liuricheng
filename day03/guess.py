import random

A=int(random.random()*2000)
i=0
while True:
    B=int(input("请输入："))
    i=i+1
    if B < A :
        print ("小")
    elif B > A:
        print("大")
    else:
        print("对","本次猜了",i,"次")
        break
