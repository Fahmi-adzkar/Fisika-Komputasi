def regula_falsi (f,a,b,tol) :
      if f(a)*f(b)>0:
            print('tebakan awal a dan b tidak mengurung akar')
            
            return None
      c = b - ((f(b)*(b-a)) / (f(b)-f(a)))
      
      while abs(f(c))>tol:
            c = b - ((f(b)*(b-a)) / (f(b)-f(a)))
            
            if f(a)*f(c)>0:
                  a=c
            if f(b)*f(c)>0:
                  b=c
      return c
