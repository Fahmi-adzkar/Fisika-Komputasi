import numpy as np
from gaussElimin import*

a=np.array([[30.0,-20.0,0.0],[-20.0,30.0,-10.0],[0.0,-10.0,10.0]])
b=np.array([20.0,40.0,60.0])

aOrig=a.copy()
bOrig=b.copy()
x=gaussElimin(a,b)
det=np.prod(np.diagonal(a))

print('x = \n',x)
print('\ndet =',det)
print('\nCheck: A*x =\n',np.dot(aOrig,x))
input("\nPress return to exit")
