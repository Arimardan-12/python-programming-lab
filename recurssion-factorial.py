def fact(a):
    if a == 1:
        return (1)
    else:
        return (a * fact(a-1))

num = int(input())
print(fact(num))