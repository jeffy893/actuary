import numpy as np

#############################################
### Note: Start varibale out with decimal ###
#############################################

# PV Solution Variable
y = 0.0
# FV Solution Variable
x = 1.0
# Accumlated Amount
A = 100.0
# Principal
P = 10000.0
# Interest Rate
i = 0.11
# Number of Terms
t = 5.0
# Present Value Interest Factor
v = (1.0/(1.0+i))
# FV Interest Favtor
w = 1.0 + i

# Simple Interest
#A = P*(1 + (i*t))
#P = A/(1 + (i*t))
#t = (A - P)/(i*P)
#i = (A - P)/(t*P)


# Compound Interest
#A = P*((1 + i)**t)
#P = A/((1 + i)**t)
#t = (np.log(A/P))/(np.log(1+i))
#i = ((A/P)**(1/t)) - 1

y = (1000.0*w**4) + (1000.0*w**5) + (1000.0*w**6)# + (1000.0*w**4)# + (1000*v**5)


print(y)
