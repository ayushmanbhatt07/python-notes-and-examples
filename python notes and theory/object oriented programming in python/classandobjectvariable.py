class abc():
    class_var=0
    def __init__(self,var): # whenever a object is created __init__() method is called to initialize it's value
        self.var=var
        abc.class_var+=1 # class local variable always to be accessed through class name 
        print("value of object variable is: ",self.var)
        print("value of class variable is: ",abc.class_var)
obj1=abc(10)
obj2=abc(20)# change in any object variable or argument passed in object doesnot affect the value of the class variable. changes made by one object are reflected in other objects as well. hence in,
# obj1 class_var=1
# obj2 class_var=2
# obj3 class_var=3

obj3=abc(30)
print("value of class attribute at last is: ",abc.class_var)