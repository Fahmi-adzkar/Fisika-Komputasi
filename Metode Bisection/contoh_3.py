def bisection(fx, a, b, err):
    if fx(a)*fx(b) < 0. :
        xi = a
        xf = b
        i = 0
        while abs((xf - xi)/xf) > err:
            xm = (xi+xf)/2.
            if fx(xi)*fx(xm) < 0: xf = xm
            else: xi = xm
            i += 1
        return xm, i
    else:
        return None, None
 
if __name__ == "__main__":
    def fx(x):
        return x**3. - 10.*x**2. + 5.
 
    res = bisection(fx, 0., 4., 1.0e-8)
    print (res)
