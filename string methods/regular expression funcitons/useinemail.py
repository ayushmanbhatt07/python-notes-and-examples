import re
emails=["test.67326@gmail.com","gkyugyuew@yahoo.com","gyjuefwgyuew@gmai_67767+++l.co67m"]
pattern=r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
for email in emails:
    if(re.match(pattern,email)):
        print("valid email:",email)
    else:
        print("not a valid email",email)