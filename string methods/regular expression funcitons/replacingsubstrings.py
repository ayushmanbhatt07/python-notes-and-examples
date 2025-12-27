import re
text="the sky is blue"
pattern="blue"
result=re.sub(pattern,"green",text)
#replaces pattern with green in text string
print(result)
