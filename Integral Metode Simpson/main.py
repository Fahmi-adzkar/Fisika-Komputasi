from simpson import *

def f(x):
    return x**2+4

a=float(input('batas bawah = '))
b=float(input('batas atas = '))
n=int(input('jumlah grid kelipatan 2 = '))

integral=simpson(f,a,b,n)

print('integral = ', integral)
