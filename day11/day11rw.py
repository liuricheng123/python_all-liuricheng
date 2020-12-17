class kt:
    __brand=None
    __price=None

    def __init__(self,b,p):
        self.__brand = b
        self.__price = p

    def setBrand(self,b):
        self.__brand = b
    def getBrand(self):
        return self.__brand

    def setPrice(self,p):
        self.__price = p
    def getPrice(self):
        return self.__price

k = kt()
k.getBrand("格力")
k.getPrice("2500")
print(k.getPrice(),k.getBrand())



