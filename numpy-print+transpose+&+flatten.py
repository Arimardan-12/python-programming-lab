import numpy as np
ar = []
a,b = map(int,input("Enter row & coloumn with space between them : ").split())
for i in range(a):
    arr = list(map(int,input("Enter the elements :\n").split()))
    ar.append(arr)
ar = np.array(ar)
print(ar.T)
print(ar.flatten())