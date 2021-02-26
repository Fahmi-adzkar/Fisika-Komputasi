import math
from bisection import *

u = 2510 
mo = 2.8 * 10**6
m = 13.3 * 10**3
g = 9.81
v = 335

def f(t):
    y = (u* math.log (mo / (mo - (m * t))) - (g * t) - v)
    return y

a=float(input('tebakan awal a = '))
b=float(input('tebakan awal b = '))
tol= float(input('toleransi = '))

t = bisection(f,a,b,tol)
print("waktu yang diperlukan roket : t =  {}".format(t))
