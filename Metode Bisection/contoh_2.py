def f(x):
    y = x**3-729
    return y

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
