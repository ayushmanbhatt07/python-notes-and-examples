class abc():
    def __init__(self,a):
        self.a=a
    def display(self):
        print("the current attribute is: ",self.a)
obj=abc(10)
obj.display()
print("check if the class has attribute a....",hasattr(obj,'a'))
getattr(obj,'a')
setattr(obj,'a',50)
print("the value of attribute after modifying/setting the newvalue for a is: ",obj.a)
setattr(obj,'b',40)
print("the value of attribute after setting the new attribute is: ",obj.b)
delattr(obj,'a')
print(obj.a) # this will throw an error as attribute a has been deleted

        