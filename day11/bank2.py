import random
bank={}
bank_name="中国工商银行昌平支行"
bank_choice={"1":"开户","2":"存钱","3":"取钱","4":"转账","5":"查询","6":"bye",}

myinfo=f'''
------------账户信息---------------
账号：{account}
姓名：{username}
密码：{password}
地址：
    国家：{country}
    省份：{province}
    街道：{street}
    门牌号：{door}
账户余额：{money}
注册银行名：{bank_name}
---------------------------------
'''
welcome='''
*********************************
*       中国工商银行账户管理系统    *
*********************************
*               选项            *
'''
welcome_item='''*           {0}.{1}             *'''
def print_welcome():
    print(welcome,end="")
    keys=bank_choice.keys()
    for i in keys:
        print+)
    print("*************************************")

def inputHelp(chose,datatype="str"):
    while True:
        print("请输入",chose,":")
        i=input(">>>:")
        if len(i)==0:
            print("该选项不能为空！请重新输入！")
            continue
        if datatype !="str":
            return int(i)
        else:
            return i
def isExists(chose,data):
    if chose in data:
        return True
    return False

def getRandom():
    li="0123456789qwertyuioplkjhgfdsazxcvbnm"
    string=""
    for i in range(8):
        string =string+li[int(random.random()*len(li))]
    return string
def findByAccount(account):
    for i in bank.keys():
        if bank[i]["account"]==account:
            return i
    return None

class User:
    __account=None
    __username=None
    __password=None
    __address=None
    __money=None
    __reg_date=None
    __bankname=None

    def __init__(self,username,password,address,money):
        self.__username=username
        self.__password=password
        self.__address=address
        self.__money=money
        self.__account=tools().getRandom






































