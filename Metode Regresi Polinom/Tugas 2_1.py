import numpy as np
import matplotlib.pyplot as plt
from polyFit import *

# input data
xData = np.array([10004.0, 20025.0, 30054.0, 40078.0, 50102.0])
yData = np.array([0.003, 0.01, 0.018, 0.0256, 0.032])

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
