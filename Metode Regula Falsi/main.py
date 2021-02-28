from regula_falsi import *

def f(x):
      y=x**2-4
      return y

a=float(input('Tebakan awal a = '))
b=float(input('Tebakan awal b = '))
tol=float(input('Toleransi = '))

x = regula_falsi(f,a,b,tol)

print ("Akar : x = {}".format(x))
