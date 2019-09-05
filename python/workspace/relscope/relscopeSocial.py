from scipy.stats import rv_continuous
import numpy as np
from scipy.special import factorial
from scipy.integrate import quad
import decimal


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

class met(rv_continuous):
    "Normal Distribution"
    def _pdf(self, x):
        #peak = 3
        # c = b^2/4a + ln(-a/pi)/2
        b = 0
        d = np.sqrt(1/(2*np.pi))
        c = np.log(d)
        y = (np.exp((-((x-4)**2)/2) + b*x + c))#*(peak/d)
        return y
met = met(name='met', a=1, b=8)


# print("%.4f" % custom.mean())
sampleWork = work.rvs(size=1000)
sampleTax = taxes.rvs(size=1000)
sampleMet = met.rvs(size=1000)
# sampleSocialCapital = socialcapital.rvs(size=1000)

#for i in range(0,30):
#    s = float(sampleScope[i])
#    c = float(sampleCapital[i])
#    sc = 0.4118 * float(sampleSocialCapital[i])
#    print(str(i) + ":   Scope = " + str(s) + " , Capital = " + str(c) + " , Social Capital = " + str(sc))

for i in range(0,1000):
    w = 8.5*float(sampleWork[i])
    t = 4.7059*float(sampleTax[i])
    m = float(sampleMet[i])
    social = 2.3529*w + t + 20*m
    # sc = 0.4118 * float(sampleSocialCapital[i])
    if((float(sampleWork[i]) != 30) & (float(sampleWork[i]) != 1) & (float(sampleTax[i]) != 30) & (float(sampleTax[i]) != 1) & (float(sampleMet[i]) != 1) & (float(sampleMet[i]) != 8)):
        print(str(w) + "," + str(t) + "," + str(m) + "," + str(social)) #+ "," + str(sc))
