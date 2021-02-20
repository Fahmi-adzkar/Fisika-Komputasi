## module euler
''' X,Y = integrate(F,x,y,xStop,h).
    Metode Euler untuk mencari solusi persamaan diferensial biasa
    {y}' = {F(x,{y})}, dimana
    {y} = {y[0],y{1},...y[n-1]}.
    x,y = Kondisi awal
    xStop = Nilai x akhir
    h = increment (interval) x
    F = fungsi yang ingin dipercahkan
        array F(x,y) = {y'[0],y'[1],...,y'[n-1]}.
'''

import numpy as np
def integrate(F,x,y,xStop,h):

    def euler(F,x,y,h):
        K0 = h*F(x,y)
        return K0
    X = []
    Y =[]
    X.append(x)
    Y.append(y)
    while x < xStop:
        h = min(h,xStop - x)
        y = y + euler(F,x,y,h)
        x = x + h
        X.append (x)
        Y.append (y)
    return np.array(X),np.array(Y)
    
