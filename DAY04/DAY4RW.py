'''
当输入54321时，求结果
num = int(input("请输入一个数："))
while num != 0:
    print(num%10)
    num=num//10
'''
k = 1
a=int(input("请输入"))
for j in range(1,a+1):
    if a==1:
      print(j,"x",a,"=",(a*j),"\t",end="")
      j+1
    break
    elif k <= j:
       print("* ", end="")
        k = k + 1
    i = i + 1
    print()


'''
    阶乘
'''
'''
sum=0
for i in range(1,21):
    sum1=1
    for i in range(1,i+1):
        sum1=sum1*i
    sum=sum1+sum
print(sum)
'''
    


'''
10个数
'''
'''
max=0
sum=0

for i in range(10):
    num=int(input("请输入数据："))
    if num>max:
        max = num
    sum=sum+num
print("最大值为：",max,",和为：",sum,"平均数为：",(sum/10))
'''



















