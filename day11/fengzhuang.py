# class person:
#     __username=""
#     __age=None
#     def setUsername(self,u):
#         self.__username=u
#
#     def setAge(self,a):
#         if a ==None:
#             print("年龄非法")
#         elif a >120 or a <0:
#             print("年龄非法")
#         else:
#             self.__age=a
#     def show(self):
#             print("我叫",self.__username,"，我的年龄为：",self.__age)
#
# p=person()
#
# p.setUsername("123")
# p.setAge(-13)
# p.show()

class Dog:
    __color=None
    __speed=None
    __belong=None


    def __init__(self,c,b,s):
        self.__color=c
        self.__speed=s
        self.__belong=b

    def setColor(self,c):
        self.__color=c
    def getColor(self):
        return self.__color

    def setSpeed(self,s):
        self.__speed=s
    def getSpeed(self):
        return self.__speed

    def setBelong(self,b):
        self.__belong=b
    def getBelong(self):
        return self.__belong

d=Dog("红色","犬科","50km/h")

print(d.getColor(),d.getBelong(),d.getSpeed())

