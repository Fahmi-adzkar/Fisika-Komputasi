import matplotlib.pyplot as plt

from polyFit import *

# input data
xData = array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0])
yData = array([20.0, 40.0, 60.0, 80.0, 100.0, 120.0, 140.0, 160.0, 180.0])
while True:
    try:
        m = eval(input("\nPolinomial Orde ==> "))
        coeff = polyFit(xData, yData, m)
        print("Koefisien :\n", coeff)
        print("Std. deviasi = ", stdDev(coeff, xData, yData))
        m = len(coeff)
        x1 = min(xData)
        x2 = max(xData)
        dx = (x2 - x1) / 20.0
        x = arange(x1, x2 + dx / 10.0, dx)
        y = zeros((len(x))) * 1.0
        for i in range(m):
            y = y + coeff[i] * x ** i
        plt.plot(xData, yData, 'o', x, y, '-')
        plt.title('Grafik Kecepatan vs Waktu')
        plt.xlabel('Waktu (s)')
        plt.ylabel('Kecepatan (m/s)')
        plt.legend(('Data', 'Regresi Polinom'), loc=0)
        plt.grid(True)
        plt.show()
    except SyntaxError:
        break
input("Finished. Press return to exit")
