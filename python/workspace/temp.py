from sympy import *
init_printing(use_unicode=False)

x = symbols('x')


y = -5*x**4 +16*x**3 - 15*x**2 + 4*x
f = -x**5 + 4*x**4 - 5*x**3 + 2*x**2

#print(y.subs(x, 2))

plot(f, (x, -5, 5))

