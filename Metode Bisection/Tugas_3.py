'''
Jika T_3 = 75, maka tentukan besar T_1 dan T_2 dengan metode Bisection !

150*cos(T_1) + 180*cos(T_2) - 200*cos(75) = 200
150*sin(T_1) + 180*sin(T_2) - 200*sin(75) = 0

'''
import cmath

def f(x):
    y = ((cmath.acos(180**2) + (200**2 - 150)) / (2*(180*200))) - x
    return y

print("Solusi Numerik untuk tugas ketiga")

a=float(input('tebakan awal a = '))
b=float(input('tebakan awal b = '))
tol= float(input('toleransi = '))

def bisection(f,a,b,tol):
    if f(a)*f(b)>0:
        print ("a dan b tidak mengurung akar, tentukan nilai lain")
        return None
    c=(a+b)/2
    while abs (f(c))>tol:
        c=(a+b)/2
        if f(a)*f(c)>0:
            a=c
        if f(b)*f(c)>0:
            b=c
    return c

x = bisection(f,a,b,tol)
print("akar persamaan: x =  {}".format(x))

