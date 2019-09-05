from scipy.stats import rv_continuous
import numpy as np
from scipy.special import factorial
from scipy.integrate import quad
import decimal


class age(rv_continuous):
    "Skewed Right Distribution"
    def _pdf(self, k):
        # Peak of distribution
        # peak = 5

        # l is the k value where the peak will be at
        l = 4

        y = decimal.Decimal((( ( l**k ) * np.exp(-l)  ) / factorial(k)))#*(b)
        return y
age = age(name='age', a=1, b=30)


class taxes(rv_continuous):
    "Skewed Left Distribution"
    def _pdf(self, k):
        # Peak of distribution
        #peak = 5

        # l is the k value where the peak will be at
        l = 17

        # Constant that sets the peak
        # b = ((factorial(l))*(exp(l)) / (l**l)) * peak

        y = decimal.Decimal((( ( l**k ) * np.exp(-l)  ) / factorial(k)))# *(b)
        return y
taxes = taxes(name='taxes', a=1, b=30)


# print("%.4f" % custom.mean())
sampleAge = age.rvs(size=1000)
sampleTaxes = taxes.rvs(size=1000)
# sampleSocialCapital = socialcapital.rvs(size=1000)

#for i in range(0,30):
#    s = float(sampleScope[i])
#    c = float(sampleCapital[i])
#    sc = 0.4118 * float(sampleSocialCapital[i])
#    print(str(i) + ":   Scope = " + str(s) + " , Capital = " + str(c) + " , Social Capital = " + str(sc))

for i in range(0,1000):
    a = 300*float(sampleAge[i])
    t = 4.7059*float(sampleTaxes[i])
    scope = a + 16.25*t
    # sc = 0.4118 * float(sampleSocialCapital[i])
    if((float(sampleAge[i]) != 1) & (float(sampleAge[i]) != 30) & (float(sampleTaxes[i]) != 1) & (float(sampleTaxes[i]) != 30)):
        print(str(a) + "," + str(t) + "," + str(scope)) #+ "," + str(sc))
