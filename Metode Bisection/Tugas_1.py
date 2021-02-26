'''
Sebuah muatan Q1= +4 C berjarak 10 m dari sebuah muatan Q2= +9 C.
Pada titik manakan pada garis yang menghubungkan dua muatan tersebut
yang medan listriknya sama dengan nol ?
'''

def f(x):
    y = (9 - 4)*x**2 + (2*4*10*x) - (4*100)
    return y

print("Solusi Numerik untuk tugas pertama")

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
