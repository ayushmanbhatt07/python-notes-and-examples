a='hello'
print(id(a))
b='world'
a+=b
print(id(a))
# string are immutable.hence add substract krne se new string create hogi
str1='python'
str1[0]='j'#string are immutable hence it will throw a error