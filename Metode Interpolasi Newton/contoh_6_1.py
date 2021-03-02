import numpy as np
import math
from newtonPoly import *
import matplotlib.pyplot as plt

xData = np.array([3.0,6.0,9.0])
yData = np.array([39.0,96.0,171.0])

a = coeffts(xData,yData)
print("t          s_Interp          s_Exact")
print("--------------------------------------")
x = np.arange(3.0,9.5,0.5)
n = len(x)
y = np.zeros((n,2))
yExact = np.zeros((n,2))
for i in range (n) :
    y[i,0] = evalPoly(a,xData,x[i])
    yExact[i,0] = 10*x[i] + 0.5*2*x[i]**2
    print('{:3.1f}     {:9.5f}     {:9.5f}'.format (x[i], y[i,0], yExact[i,0]))

plt.plot(xData, yData, 'o', x, y[:,0], 'h-', x, yExact[:,0], 's-')
plt.title('Perbandingan Data, Interpolasi Newton, dan Nilai Eksak')
plt.xlabel('Waktu t')
plt.ylabel('Perpindahan s')
plt.legend(('Data', 'Newton', 'Eksak'), loc = 0)
plt.show()

input("\nPress return to exit")
