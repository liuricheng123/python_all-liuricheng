# import xlrd
#
# data=xlrd.open_workbook("E:\\pytho\\xsxl\\a.xlsx")
# sheet=data.sheet_by_name("用户管理")
# print("有",sheet.nrows,"行数据！有",sheet.ncols,"列数据！")
#
# rows=sheet.nrows
# cols=sheet.ncols
#
# for i in range(rows):
#     for j in range(cols):
#         print(sheet.cell_value(i,j),"\t\t",end="")
#     print()



import xlrd

data=xlrd.open_workbook("E:\\pytho\\xsxl\\a.xlsx")
sheet=data.sheet_by_name("用户管理")
print("有",sheet.nrows,"行数据！有",sheet.ncols,"列数据！")

rows=sheet.nrows
cols=sheet.ncols
f=open("用户管理.txt","w+",encoding="utf-8")
a=[]
for i in range(rows):
    a=[]
    for j in range(cols):
        a.append(str(sheet.cell_value(i,j)).replace("0",""))
    string=",".join(a)
    f.write(string+"\n")