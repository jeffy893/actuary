import numpy as np

# Payment
c = 0.0
# Interest Rate
r = 0.0
# Time
t = 0.0
# Future Value
fv = 0.0
# Present Value
pv = 0.0

pv = c * ((1.0-(1.0/(1.0+r)**t))/r)
fv = c * (((1+r)**t)-1) / r

c = pv / ((1.0-(1.0/(1.0+r)**t))/r)
c = fv / (((1+r)**t)-1) / r
