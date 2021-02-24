def f(x):
    return x**2+4

a=float(input('batas bawah = '))
b=float(input('batas atas = '))
n=int(input('jumlah grid kelipatan 2 = '))

def simpson(f,a,b,n):
    h=(b-a)/n
    sum1=0.0  # untuk jumlah fungsi ganjil
    sum2=0.0  # untuk jumlah fungsi genap

    for i in range(1,n,2):
        x=a+i*h
        sum1=sum1+f(x)
    for i in range(2,n-1,2):
        x=a+i*h
        sum2=sum2+f(x)

    integral=(h/3)*(f(a)+4*sum1+2*sum2+f(b))

    return integral

integral=simpson(f,a,b,n)

print('integral = ', integral)
