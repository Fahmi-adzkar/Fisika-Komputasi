## module gaussElimin
'''
x = gaussElimin(a,b)
Mencari solusi [a]{b} = {x} dengan eliminasi Gauss
'''

import numpy as np

def gaussElimin(a,b):
    n=len(b)

    # Fase Eliminasi
    for k in range(0,n-1):
        for i in range(k+1,n):
            if a[i,k] != 0.0:
                lam = a [i,k]/a[k,k]
                a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
                b[i] = b[i] - lam*b[k]
    # Substitusi balik
    for k in range(n-1,-1,-1):
        b[k] = (b[k]-np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    return b
