st = input("Enter the string ")
res = ""
for i in st:
    out = st.count(i)
    if i not in res:
        print(f"{i} : {out}")
        res += i