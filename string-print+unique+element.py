st = input("Enter the string ")
res = ""
for i in st:
    out = st.count(i)
    if out == 1:
         res += i
print(res)