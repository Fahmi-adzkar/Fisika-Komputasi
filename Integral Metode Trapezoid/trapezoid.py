def trapezoid(f,a,b,n):
    h=(b-a)/n
    sum=0.0
    for i in range (1,n):
        x=a+i*h
        sum=sum+f(x)
    integral=(h/2)*(f(a)+2*sum+f(b))
    return integral
