from derivative import *

def newton_raphson (f,x,tol) :
      while abs (f (x)) > tol :
            dfdx = derivative (f,x)
            x = x - f(x) / dfdx
      return x
