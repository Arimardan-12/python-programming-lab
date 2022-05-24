import numpy as np
a,b = map(int,input("Enter row & coloumn with space between them : ").split())
ar1 = np.array(list(map(int,input("Enter 1st Array elements :\n").split()))).reshape(a,b)
ar2 = np.array(list(map(int,input("Enter 2st Array elements :\n").split()))).reshape(a,b)
print(np.add(ar1,ar2))
print(np.subtract(ar1,ar2))
print(np.floor(np.divide(ar1,ar2)))
print(np.multiply(ar1,ar2))
print(np.power(ar1,ar2))
