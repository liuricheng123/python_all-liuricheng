a=[8,1,2,13,4,45,6,7,8,36]
'''
print(a[1])
print(a[5])
print(a[7])
print("列表的长度：",len(a))
'''
max=a[0]
index=-1
sum=0
for i in range(0,len(a)):
    if a[i] >=max:
        max=a[i]
        index=i
    sum=sum+a[i]
print("a里的最大值为：",max,"，所对应的角标为：",index,"和为：",sum)


