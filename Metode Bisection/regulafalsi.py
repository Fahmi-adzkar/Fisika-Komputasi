def bisection(f,a,b,tol):
    if f(a)*f(b)>0:
        print ("a dan b tidak mengurung akar, tentukan nilai lain")
        return None
    c = b - ((f(b)*(b-a)) / (f(a)-f(b)))
    while abs (f(c))>tol:
        c = b - ((f(b)*(b-a)) / (f(a)-f(b)))
        if f(a)*f(c)>0:
            a=c
        if f(b)*f(c)>0:
            b=c
    return c
