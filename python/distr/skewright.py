from sympy import *
init_printing(use_unicode=False)
k = symbols('k', positive=True, nonzero=True)

# Peak of distribution
# peak = 5

# l is the k value where the peak will be at
l = 4

# Constant that sets the peak
# b = ((factorial(l))*(exp(l)) / (l**l)) * peak

y = (( ( l**k ) * exp(-l)  ) / factorial(k)) # *(b)

plot(y,(k,1,20))

pprint(y)
