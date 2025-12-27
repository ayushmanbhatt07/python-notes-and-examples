class abc():
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("the default init constructor")
    def __display(self):
        c=self.a+self.b
        print(c)
obj=abc(10,20)
obj._abc__display()
