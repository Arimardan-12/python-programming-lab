st = input("Enter the string ")
v = 0
d = 0
alfa = 0
w = 0
for i in st:
    if i in "AEIOUaeiou":
        v += 1
    elif 'a' <= i <='z' or 'A' <= i <='z':
        alfa += 1
    elif '0' <= i <= '9':
        d += 1
    else:
        w += 1
print(f"vovles: {v} \ndigit: {d} \nConsonants: {alfa} \nspace: {w}")
    
