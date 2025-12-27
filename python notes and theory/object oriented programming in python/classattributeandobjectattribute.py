class abc:
    even=0 # class attribute with default value=0
    def check(self,val):
        if(val%2==0):
            self.even=1 # object attribute overrides class attribute
    def evenornot(self,val):
        self.check(val) # calling a class method from another class method(both methods are of the same class)
        if(self.even==1):
            print("number is even: ",self.val)
        else:
            print("number is odd: ",self.val)
obj=abc(21)