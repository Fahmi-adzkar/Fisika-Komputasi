## module run_kut4
''' X,Y = integrate(F,x,y,xStop,h).
    Menggunakan metode runge-kutta orde 4
    untuk mencari solusi persamaan diferensial biasa 
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

    def run_kut4(F,x,y,h):
        K0 = h*F(x,y)
        K1 = h*F(x + h/2.0, y + K0/2.0)
        K2 = h*F(x + h/2.0, y + K1/2.0)
        K3 = h*F(x + h, y + K2)
        return (K0 + 2.0*K1 + 2.0*K2 + K3)/6.0
    X = []
    Y = []
    X.append(x)
    Y.append(y)
    while x < xStop:
        h = min(h,xStop - x)
        y = y + run_kut4(F,x,y,h)
        x = x + h
        X.append (x)
        Y.append (y)
    return np.array(X),np.array(Y)
    
