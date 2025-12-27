class abc():
    def __init__(self,var1,var2):
        self.var1=var1
        self.__var2=var2
    def display(self):
        print("the public variable var1 accessed within class is: ",self.var1)
        print("the private variable var2 accessed within class is: ",self.__var2)
obj=abc(10,20)
obj.display()
print("the public variable var1 accessed outside class is: ",obj.var1)
# print("the private variable var2 accessed outside class is: ",obj.__var2)
# the above line will show an error as private members can be accessed within class. if anyone needs to accessthem outside the class then the synax is: objectname._classname__privatevariablename
print("the private variable var2 accessed outside class is: ",obj._abc__var2)
