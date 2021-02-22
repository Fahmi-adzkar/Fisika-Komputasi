import numpy as np
from run_kut4 import *
from printSoln import *
import matplotlib.pyplot as plt

# input data
r=1.0e3                 # resistensi sebesar 1 kohm
e=5.0                   # nilai tegangan awal 5 volt
c=1.0e-3                # kapasitansi sebesar 1 mF

# y adalah tegangan
# persamaan diferensial biasa
def F(x,y):
    F = np.zeros(1)
    F[0] = (1/(r*c))*(e-y[0])
    return F
x = 0.0 # Start of integration
xStop = 20.0 # End of integration
y = np.array([0.0]) # Initial values of (y)
h = 0.1 # Step size
freq = 1
# solusi numerik menggunakan Runge-Kutta orde4
X,Y = integrate(F,x,y,xStop,h)

# memprint nilai solusi runge-kutta
print("---SOLUSI PDB METODE RUNGE KUTTA ORDE 4---")
print("-----------------------------------------")
printSoln(X,Y,freq)
print("-----------------------------------------")

#memplot Grafik Pengisian Muatan Kapasitor Rangkaian RC
plt.plot(X,Y[:,0],'o')
plt.grid(True)
plt.title('Grafik Pengisian Muatan Kapasitor Rangkaian RC')
plt.xlabel('Waktu,t (s)'); plt.ylabel('Tegangan, V(volt)')
plt.show()
input("Press return to exit")
