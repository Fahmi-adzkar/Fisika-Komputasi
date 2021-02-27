def derivative (f,x,dx=1e-10) :
      dfdx = (f (x+dx) - f (x-dx)) / (2*dx)
      return dfdx
