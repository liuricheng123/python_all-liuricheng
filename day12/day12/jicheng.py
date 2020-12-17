# class OldPhone:
#     phoneNumber=None
#     vioce=None
#
#     def call(self,number):
#         print(self.phoneNumber,"正在给",number,"打电话")
#
# nokia=OldPhone()
# nokia.phoneNumber="12345678912"
# nokia.vioce="凤凰传奇"
#
# nokia.call("32145698745")

import time
class Animal:
    __color=""
    __weight=""
    __age=None

    def __init__(self,color,weight,age):
        self.__color=color
        self.__weight=weight
        self.__age=age

    def setColor(self,color):
        self.__color=color
    def getColor(self):
        return self.__color

    def setWeight(self,weight):
        self.__weight=weight
    def getWeight(self):
        return self.__weight

    def setAge(self,age):
        self.age=age
    def getAge(self):
        return self.__age

class Dog(Animal):
    __brand=""

    def __init__(self,color,age,weight,brand):
        super().__init__(color,weight,age)
        self.__brand=brand
    def setBrand(self,brand):
        self.__brand=brand
    def getBrand(self):
        return self.__brand

    def show(self):
        for i in range(10):
            print("汪",end="")
            time.sleep(2)
        print(self.getColor(),self.getAge(),self.getWeight(),self.getBrand())

d=Dog("黄色",10,5,"犬科")
d.show()
