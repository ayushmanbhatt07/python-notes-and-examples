class abc():
    val=10
    def say(self):
        print("self default argument")
obj=abc()
obj.say()
print(obj.val())