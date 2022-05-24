a=int(input('enter the first number:'))
b=int(input('enter the second number:'))
c=int(input('enter the third number:'))

if a>b and a>c:
    print('greater number is',a)
elif b>a and b>c:
    print('greater number is',b)
else:
    print('greater number is',c)