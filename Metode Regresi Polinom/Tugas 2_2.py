import numpy as np
import matplotlib.pyplot as plt
from polyFit import *

'''
(0.101272*10^5)*3=30381.6
(0.203767*10^5)*3=61130.1
(0.305555*10^5)*3=91666.5
(0.407922*10^5)*3=122376.6
(0.509513*10^5)*3=152853.9
'''

# input data
xData = np.array([30381.6, 61130.1, 91666.5, 122376.6, 152853.9])
yData = np.array([0.016, 0.039, 0.058, 0.08, 0.098])

while True:
    try:
        m = eval(input("\nPolinomial Orde ==> "))
        coeff = polyFit(xData, yData, m)
        print ("Koefisien :\n", coeff)
        print ("Std. deviasi = ", stdDev(coeff, xData, yData))
        m = len(coeff)
        x1 = min(xData)
        x2 = max(xData)
        dx = (x2 - x1) / 20.0
        x = np.arange(x1, x2 + dx/10.0, dx)
        y = np.zeros((len(x)))*1.0
        for i in range (m):
            y = y + coeff[i]*x**i
        plt.plot(xData, yData, 'o-', x, y, '-')
        plt.title('Grafik Laser Kisi 1')
        plt.xlabel('r/d')
        plt.ylabel('x')
        plt.legend(('Data','Regresi Polinom'), loc = 0)
        plt.grid(True)
        plt.show()
    except SyntaxError : break
input("Finished. Press return to exit")
