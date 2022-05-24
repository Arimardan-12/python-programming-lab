import numpy as np
a,b=map(int,input("Enter row & coloumn with space between them : ").split())
ar = np.eye(a,b)
print(ar)