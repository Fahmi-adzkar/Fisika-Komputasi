import numpy as np
from printSoln import *
from euler import *
import matplotlib.pyplot as plt

# input data
g=9.8

# persamaan diferensial biasa
def F(x,y):
    F = np.zeros(2)
    F[0] = y[1]
    F[1]= g
    return F
x = 0.0 # Start of integration
xStop = 10.0 # End of integration
y = np.array([0.0,0.0]) # Initial values of (y)
h = 0.1 # Step size
freq = 1
# solusi numerik menggunakan Euler
X,Y = integrate(F,x,y,xStop,h)

# solusi eksak
Yexact = (1/2)*g*X*X;

# memprint nilai solusi euler dan eksak
print("---SOLUSI PDB MENGGUNAKAN METODE EULER---")
print("-----------------------------------------")
printSoln(X,Y,freq)
print("-----------------------------------------")

#memplot nilai solusi euler dan eksak
plt.plot(X,Y[:,0],'o',X,Yexact,'-')
plt.grid(True)
plt.title('Grafik Gerak Jatuh tanpa Gesekan Udara')
plt.xlabel('Waktu,t (s)'); plt.ylabel('Posisi, y(m)')
plt.legend(('Euler','Exact'),loc=0)
plt.show()
input("Press return to exit")
