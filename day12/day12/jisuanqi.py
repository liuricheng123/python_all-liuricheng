class counter:
    __jia=""
    __jian=""
    __cheng=""
    __chu=""
    a=input(print("请输入第一个数："))
    b=input(print("请输入第二个数："))
    def __init__(self,jia,jian,cheng,chu):
        self.__jia=jia
        self.__jian=jian
        self.__cheng=cheng
        self.__chu=chu

    def setJia(self,jia):
        # a=input(print("请输入第一个数："))
        # b=input(print("请输入第二个数："))
        self.__jia = jia
    def getJia(self):
        return self.__jia

    def setJian(self,jian):
        # a=input(print("请输入第一个数："))
        # b=input(print("请输入第二个数："))
        self.__jian=jian
    def getJian(self):
        return self.__jian

    def setCheng(self,cheng):
        # a=input(print("请输入第一个数："))
        # b=input(print("请输入第二个数："))
        self.__cheng=cheng
    def getCheng(self):
        return self.__cheng

    def setChu(self,chu):
        # a=input(print("请输入第一个数："))
        # b=input(print("请输入第二个数："))
        self.__chu=chu
    def getChu(self):
        return self.__chu

    def show(self):
        print(self.getJia(),self.__jian,self.__cheng,self.__chu)
j=counter()
j.show()






