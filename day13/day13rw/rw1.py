from day13rw.AgeException import AgeException
class person:
    __age=None

    def setAge(self,age):
        self.__age=age
    def getAge(self):
        return self.__age

    def age(self):
        if self.__age>0:
            print(self.__age)
        else:
            raise AgeException("输入非法！")


