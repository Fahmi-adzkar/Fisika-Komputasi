'''
Tentukan waktu yang diperlukan sebuah roket untuk mencapai kecepatan suara ?
'''

from regula_falsi import *
import math

u = 2510 
mo = 2.8 * 10**6
m = 13.3 * 10**3
g = 9.81
v = 335

def f(x):
      y=(u* math.log (mo / (mo - (m * x))) - (g * x) - v)
      return y

a=float(input('Tebakan awal a = '))
b=float(input('Tebakan awal b = '))
tol=float(input('Toleransi = '))

x = regula_falsi(f,a,b,tol)

print ("Waktu yang diperlukan roket : t = {}".format(x))
