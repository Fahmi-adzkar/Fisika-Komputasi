import numpy as np
import math
from newtonPoly import *
import matplotlib.pyplot as plt

B = 2 # Besar Medan Magnet
A = 2 # Besar Arus

xData = np.array([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0])
yData = np.array([2.0,4.0,6.0,8.0,10.0,12.0,14.0,16.0,18.0,20.0])

a = coeffts(xData,yData)
print("t          s_Interp          s_Exact")
print("--------------------------------------")
x = np.arange(1.0,11.0,1.0)
n = len(x)
y = np.zeros((n,2))
yExact = np.zeros((n,2))
for i in range (n) :
    y[i,0] = evalPoly(a,xData,x[i])
    yExact[i,0] = B*A*x[i]*0.5
    print('{:3.1f}     {:9.5f}     {:9.5f}'.format (x[i], y[i,0], yExact[i,0]))

plt.plot(xData, yData, 'o', x, y[:,0], 'h-', x, yExact[:,0], 's-')
plt.title('Perbandingan Data Interpolasi Newton dan Nilai Eksak')
plt.xlabel('Panjang Kawat (m)')
plt.ylabel('Gaya Lorentz (N)')
plt.legend(('Data', 'Newton', 'Eksak'), loc = 0)
plt.show()

input("\nPress return to exit")
