from sympy import *

x, t, z, nu = symbols('x t z nu')

# Pretty Printing
init_printing(use_unicode=False)


# Derivative
diff(sin(x)*exp(x), x)

# Integral
integrate(exp(x)*sin(x) + exp(x)*cos(x), x)

# Integral with lower and upper bound
# Raise to a power is "**"
# Infinity symbol is "oo"
integrate(sin(x**2), (x, -oo, oo))

# Limit
limit(sin(x)/x, x, 0)


# Solve
solve(x**2 - 2, x)

# Solve differential equation
y = Function('y')
dsolve(Eq(y(t).diff(t, t) - y(t), exp(t)), y(t))


# Eigenvalue
Matrix([[-2,2], [2,-5]]).eigenvals()


# Bessel function
besselj(nu, z).rewrite(jn)

# Print LATEX
latex(Integral(cos(x)**2, (x, 0, pi)))
