from scipy.stats import rv_continuous
import numpy as np
from scipy.special import factorial
import decimal
class scope(rv_continuous):
    "Normal Distribution"
    def _pdf(self, x):
        #peak = 3
        # c = b^2/4a + ln(-a/pi)/2
        b = 0
        d = np.sqrt(1/(72*np.pi))
        c = np.log(d)
        y = (np.exp((-((x-35)**2)/72) + b*x + c))#*(peak/d)
        return y
scope = scope(name='scope', a=1, b=100)


class capital(rv_continuous):
    "Skewed Right Distribution"
    def _pdf(self, k):
        # Peak of distribution
        # peak = 5

        # l is the k value where the peak will be at
        l = 4

        y = decimal.Decimal((( ( l**k ) * np.exp(-l)  ) / factorial(k)))#*(b)
        return y
capital = capital(name='capital', a=1, b=30)


class socialcapital(rv_continuous):
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
socialcapital = socialcapital(name='socialcapital', a=1, b=30)



# print("%.4f" % custom.mean())
sampleScope = scope.rvs(size=1000)
sampleCapital = capital.rvs(size=1000)
sampleSocialCapital = socialcapital.rvs(size=1000)

#for i in range(0,30):
#    s = float(sampleScope[i])
#    c = float(sampleCapital[i])
#    sc = 0.4118 * float(sampleSocialCapital[i])
#    print(str(i) + ":   Scope = " + str(s) + " , Capital = " + str(c) + " , Social Capital = " + str(sc))

for i in range(0,1000):
    s = float(sampleScope[i])
    c = float(sampleCapital[i])
    sc = 0.4118 * float(sampleSocialCapital[i])
    print(str(s) + "," + str(c) + "," + str(sc))
