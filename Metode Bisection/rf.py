from regulafalsi import *

def f(x):
    y = x**2-4
    return y

a=float(input('tebakan awal a = '))
b=float(input('tebakan awal b = '))
tol= float(input('toleransi = '))

x = bisection(f,a,b,tol)
print("akar persamaan: x =  {}".format(x))
