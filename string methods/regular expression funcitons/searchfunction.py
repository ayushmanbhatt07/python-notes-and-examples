import re
test="learning python is fun"
pattern="python"
result=re.search(pattern,test)
# print(result)
if result:
    print(f"match found at {result.start()}")
else:
    print("no match")