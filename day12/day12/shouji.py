'''
class phone:
    __a=None
    __b=None
    __c=None

    def __init__(self,a,b,c):
        self.__a=a
        self.__b=b
        self.__c=c
    def seta(self,a):
        self.__a=a
    def geta(self):
        return self.__a
    def setb(self,b):
        self.__b=b
    def getb(self):
        return self.__b
    def setc(self,c):
        self.__c=c
    def getc(self):
        return self.__c
    def show(self):
        print(self.geta(),self.getb(),self.getc())
p=phone("123456789","987654321","格力")
p.show()
'''
import time
class oldphone:
    phoneNumber=None
    brand=None

    def call(self,number):
        print(self.phoneNumber,"正在给",number,"打电话......")

class NewPhone(oldphone):

    def __init__(self,phoneNumber,brand):
        super().__init__(phoneNumber,brand)

    def shou(self):
        for i in range(6):
            print("嘟",end="")
            time.sleep(1)
    print("")


























