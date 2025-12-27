class abc():
    def __init__(self,a,b):
        print("default method initializer")
        self.a=a
        self.b=b
    def add(self):
        c=self.a+self.b
        print(c)
obj=abc(10,20)
print(obj.add())
print("class variables are: ",obj.a,obj.b)
obj.new_var=30 # adding a variable to class at runtime
print("the new class varibale is",obj.new_var)
obj.new_var=40 # modifying new class variable
print("modified new class variable is: ",obj.new_var)
del obj.new_var #the newly created variable is deleted
print(obj.new_var) # this would throw an error as obj.new_var has been deleted
