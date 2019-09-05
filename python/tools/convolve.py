from sympy import *
init_printing(use_unicode=False)

k = symbols('k')


def convolve(f, g, x, lower_limit, upper_limit):
    y = Symbol('y')
    h = g.subs(x, x - y)
    return integrate(f * h, (y, lower_limit, upper_limit))

l = 4

y1 = 300*(( ( l**k ) * exp(-l)  ) / factorial(k))

j = 17

y2 = 4.7059*(( ( j**k ) * exp(-j)  ) / factorial(k))


print(simplify(convolve(y1,y2,k, 0, k)))
