st = input("Enter the string ")
res = ""
for i in st:
    if i not in res:
        res += i
print(res)