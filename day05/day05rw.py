#a=[1,5,21,30,15,9,30,24]
#对列表中数字是5的倍数进行求和

sum=0
a=[1,5,21,30,15,9,30,24]
for i in range(0,len(a)):
    if a[i]%5==0:
        sum=sum+a[i]
print(sum)
print(sorted (a))


