'''
Sebuah muatan Q1= +4 C berjarak 10 m dari sebuah muatan Q2= +9 C.
Pada titik manakan pada garis yang menghubungkan dua muatan tersebut
yang medan listriknya sama dengan nol ?
'''

from newton_raphson import*

def f (x) :
      y=(9 - 4)*x**2 + (2*4*10*x) - (4*100)
      return y

x_i = float(input(" Tebakan awal akar, xi = "))
tol = float(input(" Toleransi = "))

x = newton_raphson (f, x_i, tol)

print("Akar persamaan: x =  {}".format(x))
