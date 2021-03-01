import numpy as np
from gaussElimin import*
'''
np.cos(-30) = 0.15425
np.cos(60) = -0.95241
'''

a=np.array([[0.15425,0.0, -0.95241],[-0.15425,1.0,0.0],[0.0,-1.0,0.95241]])
b=np.array([0.0,0.0,0.0])

aOrig=a.copy()
bOrig=b.copy()
x=gaussElimin(a,b)
det=np.prod(np.diagonal(a))

print('x = \n',x)
print('\ndet =',det)
print('\nCheck: A*x =\n',np.dot(aOrig,x))
input("\nPress return to exit")
