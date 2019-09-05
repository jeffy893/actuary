from scipy.stats import rv_continuous
import numpy as np
class custom(rv_continuous):
    "Custom Distribution"
    def _pdf(self, x):
        #peak = 3
        # c = b^2/4a + ln(-a/pi)/2
        b = 0
        d = np.sqrt(1/(2*np.pi))
        c = np.log(d)
        y = (np.exp((-(x**2)/2) + b*x + c))#*(peak/d)
        return y
custom = custom(name='custom')

print("%.4f" % custom.mean())


'''
rvs(*args, **kwds)	Random variates of given type.
pdf(x, *args, **kwds)	Probability density function at x of the given RV.
logpdf(x, *args, **kwds)	Log of the probability density function at x of the given RV.
cdf(x, *args, **kwds)	Cumulative distribution function of the given RV.
logcdf(x, *args, **kwds)	Log of the cumulative distribution function at x of the given RV.
sf(x, *args, **kwds)	Survival function (1 - cdf) at x of the given RV.
logsf(x, *args, **kwds)	Log of the survival function of the given RV.
ppf(q, *args, **kwds)	Percent point function (inverse of cdf) at q of the given RV.
isf(q, *args, **kwds)	Inverse survival function (inverse of sf) at q of the given RV.
moment(n, *args, **kwds)	n-th order non-central moment of distribution.
stats(*args, **kwds)	Some statistics of the given RV.
entropy(*args, **kwds)	Differential entropy of the RV.
expect([func, args, loc, scale, lb, ub, ...])	Calculate expected value of a function with respect to the distribution.
median(*args, **kwds)	Median of the distribution.
mean(*args, **kwds)	Mean of the distribution.
std(*args, **kwds)	Standard deviation of the distribution.
var(*args, **kwds)	Variance of the distribution.
interval(alpha, *args, **kwds)	Confidence interval with equal areas around the median.
__call__(*args, **kwds)	Freeze the distribution for the given arguments.
fit(data, *args, **kwds)	Return MLEs for shape (if applicable), location, and scale parameters from data.
fit_loc_scale(data, *args)	Estimate loc and scale parameters from data using 1st and 2nd moments.
nnlf(theta, x)	Return negative loglikelihood function.
'''
