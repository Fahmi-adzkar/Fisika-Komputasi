import numpy as np
import math
from newtonPoly import *
import matplotlib.pyplot as plt

pv = 8.85*pow(10,-12)
kk = 0.001

xData = np.array([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0])
# yData = np.array([0.00000000885,0.0000000177,0.00000002655])
yData = np.array([8.85*pow(10,-9),1.77*pow(10,-8),
                  2.655*pow(10,-8),3.54*pow(10,-8),
                  4.425*pow(10,-8),5.31*pow(10,-8),
                  6.195*pow(10,-8),7.08*pow(10,-8),
                  7.965*pow(10,-8),8.85*pow(10,-8)])

a = coeffts(xData,yData)
print("t          s_Interp          s_Exact")
print("--------------------------------------")
x = np.arange(1.0,11.0,1.0)
n = len(x)
y = np.zeros((n,2))
yExact = np.zeros((n,2))
for i in range (n) :
    y[i,0] = evalPoly(a,xData,x[i])
    yExact[i,0] = pv*x[i] / kk
    print('{:3.1f}     {:9.5f}     {:9.5f}'.format (x[i], y[i,0], yExact[i,0]))

plt.plot(xData, yData, 'o', x, y[:,0], 'h-', x, yExact[:,0], 's-')
plt.title('Data Interpolasi Newton dan Nilai Eksak')
plt.xlabel('Luas Penampang Keping A (m^2)')
plt.ylabel('Kapasitas Kapasitor C (F)')
plt.legend(('Data', 'Newton', 'Eksak'), loc = 0)
plt.show()

input("\nPress return to exit")
