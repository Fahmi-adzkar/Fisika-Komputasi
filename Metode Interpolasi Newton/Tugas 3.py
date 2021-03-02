import numpy as np
import math
from newtonPoly import *
import matplotlib.pyplot as plt

V = 10 # Volume
n = 1000.0 / 14.0067 # Mol gas
R = 8.314472 # Konstanta Gas ideal

xData = np.array([-40.0,0.0,40.0,80.0,120.0,160.0,200.0])
yData = np.array([6900.0,8100.0,9300.0,10500.0,11700.0,12900.0,14100.0])

a = coeffts(xData,yData)
print("t          s_Interp          s_Exact")
print("--------------------------------------")
x = np.arange(-40.0,240.0,40.0)
n = len(x)
y = np.zeros((n,2))
yExact = np.zeros((n,2))
for i in range (n) :
    y[i,0] = evalPoly(a,xData,x[i])
    yExact[i,0] = n*R*x[i] / V
    print('{:3.1f}     {:9.5f}     {:9.5f}'.format (x[i], y[i,0], yExact[i,0]))

plt.plot(xData, yData, 'o', x, y[:,0], 'h-', x, yExact[:,0], 's-')
plt.title('Perbandingan Data Interpolasi Newton dan Nilai Eksak')
plt.xlabel('Temperatur (C)')
plt.ylabel('Tekanan (N/m^2)')
plt.legend(('Data', 'Newton', 'Eksak'), loc = 0)
plt.show()

input("\nPress return to exit")
