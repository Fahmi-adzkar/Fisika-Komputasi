'''
Sebuah muatan Q1= +4 C berjarak 10 m dari sebuah muatan Q2= +9 C.
Pada titik manakan pada garis yang menghubungkan dua muatan tersebut
yang medan listriknya sama dengan nol ?
'''

from regula_falsi import *

def f(x):
      y=(9 - 4)*x**2 + (2*4*10*x) - (4*100)
      return y

a=float(input('Tebakan awal a = '))
b=float(input('Tebakan awal b = '))
tol=float(input('Toleransi = '))

x = regula_falsi(f,a,b,tol)

print ("Akar : x = {}".format(x))
