'''
Tentukan waktu yang diperlukan sebuah roket untuk mencapai kecepatan suara ?
'''

from newton_raphson import*
import math

u = 2510 
mo = 2.8 * 10**6
m = 13.3 * 10**3
g = 9.81
v = 335

def f (x) :
      y=(u* math.log (mo / (mo - (m * x))) - (g * x) - v)
      return y

x_i = float(input(" Tebakan awal akar, xi = "))
tol = float(input(" Toleransi = "))

x = newton_raphson (f, x_i, tol)

print("Waktu yang diperlukan roket : t =  {}".format(x))
