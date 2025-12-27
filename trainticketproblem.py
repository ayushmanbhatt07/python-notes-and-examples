"""Write a Class ‘Train’ which has methods to book a ticket, get status (no. of seat) 
and get fare information of train running under Indian Railways. """
import random
class train:
    def __init__(self,trainno):
        self.trainno=trainno
    def trainnum(self):
        print(f"Your train number is: {self.trainno}")
    def fareinfo(self):
        print(f"Your train from surat to mumbai is booked. Your Fare is: {random.randint(250,4000)}")
a=random.randint(2340,30000)
obj=train(a)
obj.fareinfo()
obj.trainnum()
   
        