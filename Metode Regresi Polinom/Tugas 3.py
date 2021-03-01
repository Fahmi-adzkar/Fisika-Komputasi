import matplotlib.pyplot as plt

from polyFit import *

# input data
xData = array([60.0, 120.0, 180.0, 240.0, 300.0, 360.0, 420.0, 480.0, 540.0, 600.0])
yData = array([2.6, 3.1, 4.6, 6.5, 8.5, 11.0, 15.2, 34.7, 65.8, 69.4])
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
        plt.plot(xData, yData, 'o-', x, y, '-')
        plt.title('Grafik Waktu vs Perubahan Suhu')
        plt.xlabel('Waktu (s)')
        plt.ylabel('Suhu (Celcius)')
        plt.legend(('Data', 'Regresi Polinom'), loc=0)
        plt.grid(True)
        plt.show()
    except SyntaxError:
        break
input("Finished. Press return to exit")
