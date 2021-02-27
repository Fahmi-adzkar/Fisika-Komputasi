from newton_raphson import*

def f (x) :
      y=x**2-4
      return y

x_i = float(input(" Tebakan awal akar, xi = "))
tol = float(input(" Toleransi = "))

x = newton_raphson (f, x_i, tol)

print("Akar persamaan: x =  {}".format(x))


