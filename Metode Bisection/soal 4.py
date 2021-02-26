def f(V):
    y = V**2 - 6.598791269 # ((1.5*0.092*298) - (2.25*1.39)/ 1 *(5.79 - 0.0319))
    return y

# R = 0.092
# n = (1.5)**2 = 2.25
# a = 1.39
# b = 0.0319
# v = 33.6
# p = 1
# T = 298


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

V = bisection(f,a,b,tol)

print("akar persamaan: V =  {}".format(V))
