import numpy as np
import scipy.stats as st                                                                                        
class my_pdf(st.rv_continuous):
    def _pdf(self,x):
        #peak = 3
        b = 0
        d = np.sqrt(1/(2*np.pi))
        c = np.log(d)
        return (np.exp((-(x**2)/2) + b*x + c))#*(peak/d)

my_cv = my_pdf(a=-10, b=10, name='my_pdf')


print(my_cv.mean())
