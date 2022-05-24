def count(st):
    c = 0
    v = 0
    st = st.lower()
    for i in st:
        if i in 'aieou':
            v += 1
        elif 96 < ord(i) < 122:
            c += 1
    print('Count of vowels = ',v)
    print('Count of consonents = ',c)

str = input('Enter the string ')
count(str)