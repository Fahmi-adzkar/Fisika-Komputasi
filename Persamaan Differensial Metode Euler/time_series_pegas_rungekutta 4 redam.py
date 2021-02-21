import numpy as np
from printSoln import *
from run_kut4 import *
import matplotlib.pyplot as plt

# input data
k=2.00
m=2.00
b=1.00

# persamaan diferensial biasa
def F(x,y):
    F = np.zeros(2)
    F[0] = y[1]
    F[1]= -(k/m)*y[0]-(b/m)*y[1]
    return F
x = 0.0 # Start of integration
xStop = 20.0 # End of integration
y = np.array([0.02,0]) # Initial values of (y)
h = 0.1 # Step size
freq = 1
# solusi numerik menggunakan Runge-Kutta orde4
X,Y = integrate(F,x,y,xStop,h)

# memprint nilai solusi numerik
print("---METODE NUMERIK Rungge-kutta 4th order---")
print("-----------------------------------------")
printSoln(X,Y,freq)
print("-----------------------------------------")

#memplot solusi untuk posisi
plt.subplot(2,1,1)
plt.plot(X,Y[:,0],'-')
plt.grid(True)
plt.title('Grafik posisi terhadap waktu')
plt.xlabel('Waktu,t (s)'); plt.ylabel('Posisi, y(m)')

#memplot solusi untuk posisi
plt.subplot(2,1,2)
plt.plot(X,Y[:,1],'-')
plt.grid(True)
plt.title('Grafik kecepatan terhadap waktu')
plt.xlabel('Waktu,t (s)'); plt.ylabel('kecepatan, (m/s)')
plt.show()
input("Press return to exit")
