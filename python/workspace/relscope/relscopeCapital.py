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


class work(rv_continuous):
    "Skewed Right Distribution"
    def _pdf(self, k):
        # Peak of distribution
        # peak = 5

        # l is the k value where the peak will be at
        l = 4

        y = decimal.Decimal((( ( l**k ) * np.exp(-l)  ) / factorial(k)))#*(b)
        return y
work = work(name='work', a=1, b=30)


# print("%.4f" % custom.mean())
sampleAge = age.rvs(size=1000)
sampleWork = work.rvs(size=1000)
# sampleSocialCapital = socialcapital.rvs(size=1000)

#for i in range(0,30):
#    s = float(sampleScope[i])
#    c = float(sampleCapital[i])
#    sc = 0.4118 * float(sampleSocialCapital[i])
#    print(str(i) + ":   Scope = " + str(s) + " , Capital = " + str(c) + " , Social Capital = " + str(sc))

for i in range(0,1000):
    a = 300*float(sampleAge[i])
    w = 8.5*float(sampleWork[i])
    capital = a + 38.2353*w
    # sc = 0.4118 * float(sampleSocialCapital[i])
    if((float(sampleAge[i]) != 1) & (float(sampleAge[i]) != 30) & (float(sampleWork[i]) != 1) & (float(sampleWork[i]) != 30)):
        print(str(a) + "," + str(w) + "," + str(capital)) #+ "," + str(sc))
