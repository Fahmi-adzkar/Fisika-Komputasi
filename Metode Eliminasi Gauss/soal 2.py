import numpy as np
from gaussElimin import*

a=np.array([[6.0,0.0,-1.0,0.0,0.0],[-3.0,3.0,0.0,0.0,0.0],[0.0,-1.0,9.0,0.0,0.0],[0.0,-1.0,-8.0,11.0,-2.0],
            [-3.0,-1.0,9.0,0.0,4.0]])
b=np.array([50.0,0.0,160.0,0.0,0.0])

aOrig=a.copy()
bOrig=b.copy()
x=gaussElimin(a,b)
det=np.prod(np.diagonal(a))

print('x = \n',x)
print('\ndet =',det)
print('\nCheck: A*x =\n',np.dot(aOrig,x))
input("\nPress return to exit")
