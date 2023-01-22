# str1='Md Sabbir Hosen'
# str2='md saiful mal'
# print(str1.title())
# print(str1.capitalize())
# print(str2.lower())
# print(str1.upper())
# print(str1.casefold())
# print(str1.swapcase())
# str1='PYTHON!'
# str2='I love Python'
# str3='i love python'
# str4=' '
# str5='abdulawoal'
# str6='7abdul'
# str7='pyth0n'
# print(str1.isupper())
# print(str2.istitle())
# print(str3.islower())
# print(str4.isspace)
# print(str5.isidentifier())
# print(str7.encode())
# number='12345678910'
# str1='Abdul'
# str2='$$'
# print('Al NUmber check:',number.isalnum())
# print('isnumerice:',number.isnumeric())
# print('isdechimal:',number.isdecimal())
# print('isdigit',number.isdigit())
# print('isaplha',str1.isalpha())
# print('isascii',str2.isascii())
# str1="Python is awesome, isn't it?"
# substring='i'
# print(str1.count(substring))
# print(str1.count('is'))
# str1="Bangladesh is Beautyful Country.isn't your country?"
# print(Var.endswith('ry?'))
# print(Var.startswith('B'))
# print(str1.index('is'))
# print(str1.rindex('is'))
# print(str1.find('Co3'))
# print(str1.rfind('co3'))
# str1="  Hello World  "
# str2='---Hello world---'
# print(str2.strip('-'))
# print(str2.lstrip('-'))
# print(str2.rstrip('-'))
# print(str1.strip())
# str1="Hello, My Name is kamal\n,He Is 26 Years Old"
# # print(str1.split())
# # print(str1.split(','))
# # print(str1.split(',',maxsplit=1))
# print(str1.splitlines())
# str1="Awaol"
# str2="md abdul \tawaol"
# str3="Hello World"
# str4="My name is awaol"
# # print(str1.center(20))
# # print(str1.center(20,'*'))
# # print(str1.ljust(20,'*'))
# # print(str1.rjust(20,'*'))
# print(str2.expandtabs(20))
# print(str2.expandtabs(50))
# print(str2.expandtabs(5))
# 
def urlify(string):
    stripped=string.strip()
    name=stripped.lower()
    url=name.replace(' ','-')
    return url
print(urlify('Md Abdul Hasib'))
# def urlify(string):
#     stripped=string.strip()
#     small=stripped.lower()
#     url=small.replace(' ','-')
#     return url
# print(urlify('Md Abdul awaol '))
def urlify(string):
    stripped=string.strip()
    small=stripped.lower()
    url=small.replace(' ','-')
    return url
print(urlify('Md Abdul awaol '))
def number(text):
    ret=text.strip()
    sm=ret.lower()
    take=sm.replace(' ','-')
    return take
print(number('abdul kamal'))
