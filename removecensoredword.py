l=[]
for i in range(1,5):
    a=input("enter the censored word: ")
    l.append(a)
# print(l)
with open("myfile.txt","r") as f:
    text=f.read()
# print(text)
for word in l:
    if(word in text):
        text=text.replace(word,"#####")
with open("myfile.txt","w") as f:
    f.write(text)