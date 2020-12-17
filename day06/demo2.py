'''
a="this is a dog,that is a monkey"
b=list(a)
for i in range(0,len(b)):
    count=0
    flag=True
    for k in range(0,i):
        if b[k]==b[i]:
            flag=False
            break
    if flag==False:
        continue
    for j in range(0,len(b)):
        if b[i]==b[j]:
            count+=1
print(b[i],"出现了",count,"次")
'''
'''
a="this is a dog,that is a monkey"
for index,ch in enumerate(a):
    if ch in a[:index]:
        continue
    print(ch,"出现了",a.count(ch))
'''
'''
字典形式求次数
'''
'''
li=[1,1,2,5,8,4,7,4,5,8,4,5,9,32,52,45,14]
d={}
for i in li:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)
'''
'''
def back(a,b):
    c=a+b
    return c
ba=back(55,45)
print(ba)
'''

