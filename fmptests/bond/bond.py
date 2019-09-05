import numpy as np

# Interest Rate
ytm = 0.16
# Coupon Rate
cr = 0.14
# Years
y = 7.0 
# Periods Per Year
m = 2.0
# Periods
t = y * m
# Future Value
fv = 0.0
# Present Value
pv = 0.0
# Par Value
par = 1000.0
# Coupon
cpn = (cr * par) / m
# Rate
r = ytm / m

pv = (par/((1.0 + r)**t)) + ( cpn * ((1.0-(1.0/(1.0 + r)**t))/r) )

'''
fv = c * (((1+r)**t)-1) / r

c = pv / ((1.0-(1.0/(1.0+r)**t))/r)
c = fv / (((1+r)**t)-1) / r
'''

print(pv)
