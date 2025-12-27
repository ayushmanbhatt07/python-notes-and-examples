'''A spam comment is defined as a text containing following keywords:
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
to detect these spams.'''
p1="Make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click this"
p5=p1.upper()
p6=p2.upper()
p7=p3.upper()
p8=p4.upper()
p=input("enter the comment: ")
pp=p.upper()
if((p5 in pp) or (p6 in  pp) or(p7 in pp)or(p8 in pp)):
    print("spam")
else:
    print("not a scam")
