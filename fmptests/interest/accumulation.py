import numpy as np

# Amount Function: A(t)
# Accumulation Function: a(t) = A(t)/A(0)
## Accumulation Functions have the following properties
### 1) a(0) = 1
### 2) a(t) is increasing; a'(t) > 0
### 3) dom(a) is a continuous interval (i.e. can be piece-wise)
# If $k is deposited at time s, then the accumulated value
## of $k at time t > s is: k(a(t)/a(s))
### Accumulation Factor/Growth Factor: a(t)/a(s)
# nth period of interest: I_n = A(n) - A(n-1)
# Interest starting with $k between s and t: I_{[s,t]} = A(t) - A(s) = k(a(t) - a(s))

# A(n) - A(t) = |A(n) - A(0)| - |A(t) - A(0)| = \sum_{j=t+1}^{n}I_j = \sum_{j = 1}^{n}I_j - \sum_{j = 1}^{t}I_j
# 1+2+3+...+n = n(n+1)/2


def accum(A1,A2):
    return A1/A2

def value(k,a1,a2):
    return k*(a1/a2)
