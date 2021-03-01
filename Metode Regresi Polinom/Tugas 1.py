import numpy as np
import matplotlib.pyplot as plt
from polyFit import *

# input data
xData = np.array([0.000032, 0.000031, 0.00003, 0.000026, 0.000024])
yData = np.array([0.482, 0.47, 0.458, 0.44, 0.42])

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
        plt.title('Grafik Volume vs Tinggi Permukaan')
        plt.xlabel('Volume Cairan (Q)')
        plt.ylabel('Tinggi Permukaan Air (h)')
        plt.legend(('Data','Regresi Polinom'), loc = 0)
        plt.grid(True)
        plt.show()
    except SyntaxError : break
input("Finished. Press return to exit")
        
