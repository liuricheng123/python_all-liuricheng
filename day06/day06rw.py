'''
编程实现数据列表的翻转
'''
list=[1,2,3,4,5,6,7,8,9]
for i in range(0,len(list)):
    for j in range(len(list)-1):
        if list[j]<list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
print(list)

'''
统计每个数字出现次数
a = [1,4,7,5,82,1,3,4,5,9,7,6,1,10]
for index,ba in enumerate(a):
    if ba in a[:index]:
        continue
    print(ba,"出现了",a.count(ba),"次")
'''
'''
以下数据库实现
n = [
    ["何登勇","56","男","106","IBM", 500 ,"50"],
    ["曹东雪","19","女","230","微软", 501 ,"60"],
    ["刘营营", "19", "女", "210", "Oracle", 600, "60"],
    ["李汉聪", "45", "男", "230", "Tencent", 700 , "10"]
]
#sum=names[0][5]+names[1][5]+names[2][5]+names[3][5]
#sum=int(sum)
#age=names[0][1]+[1][1]+[2][1]+[3][1]
#age=int(age)
#print(sum)
n.append(["张佳伟","45","男","220","alibaba","500","30"])
print(n)
'''


