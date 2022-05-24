def upper_case(st):
    re = ''
    for i in st:
        if 96 < ord(i) < 122:
            re = re + chr(ord(i)-32) 
        else:
            re = re + i
    return re

st = input("Enter the string ")
print(upper_case(st))
