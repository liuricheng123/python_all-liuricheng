a=[5,6,4,2,3,8,9,1,10,12]
for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j] < a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            print(a)

