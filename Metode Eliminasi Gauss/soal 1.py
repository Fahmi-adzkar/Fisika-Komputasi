import numpy as np
from gaussElimin import*

a=np.array([[2.0,4.0],[0.0,-2.0]])
b=np.array([8.0,0.0])

aOrig=a.copy()
bOrig=b.copy()
x=gaussElimin(a,b)
det=np.prod(np.diagonal(a))

print('x = \n',x)
print('\ndet =',det)
print('\nCheck: A*x =\n',np.dot(aOrig,x))
input("\nPress return to exit")
