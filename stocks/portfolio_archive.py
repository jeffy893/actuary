import numpy as np
import csv
stock1 = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
count = 0
with open('stock1.csv', 'rb') as csvfile:
    read = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in read:
        #if(count > 0):
        stock1[count] = float(row[1])
            #print row[0] + ',' + row[1]
        count = count + 1
    count = 0

stock1_returns = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
for count in range(11):
    if(count < 12):
        stock1_returns[count] = (stock1[count+1] - stock1[count])/stock1[count]

stock1_cum_ret = 0.0
for count in range(11):
    stock1_cum_ret += stock1_returns[count]

stock1_avg_daily_ret = stock1_cum_ret / 10.0

stock1_sum_squared_error = 0.0
for count in range(11):
    stock1_sum_squared_error += ((stock1_returns[count] - stock1_avg_daily_ret)**2)
stock1_variance = stock1_sum_squared_error/10.0

stock1_standard_deviation = np.sqrt(stock1_variance)

print('stock'" + i + ")
print(stock" + i + "_cum_ret)
print(stock" + i + "_variance)
print(stock" + i + "_standard_deviation)





# Portfolio Return
#port_ret = w1*r1 + w2*r2 + ... + wn*rn
#port_ret = w1*stock1_cum_ret + w2*stock2_cum_ret
# Portfolio Variance
#port_var = (w1**2)*(stock1_variance) + (w2**2)*(stock2_variance) + 2*(w1)*(w2)*(s1s2_cov)

'''
from scipy.optimize import fsolve
import math

port_ret = 0.03
def equation(p):
	w1, w2 = p
	return(w1*stock1_cum_ret + w2*stock2_cum_ret - port_ret,(w1**2)*(stock1_variance) + (w2**2)*(stock2_variance) + 2*(w1)*(w2)*(s1s2_cov))

w1, w2 = fsolve(equation, (1,1))

print(equation(w1, w2))
'''


'''

stock1[12] = {0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0}
with open('stock2.csv', 'rb') as csvfile:
    read = csv.reader(csvfile, delimiter=',', quotechar='"')
    count = 0
    for row in read:
        #if(count > 0):
        stock2[count] = row[1]
            #print row[0] + ',' + row[1]
        count = count + 1
    count = 0
'''


s1s2_squared_error = 0.0
for count in range(11):
	s1s2_squared_error += (stock1_returns[count] - stock1_avg_daily_ret)*(stock1_returns[count] - stock1_avg_daily_ret)
s1s2_cov = s1s2_squared_error / 10.0




from scipy.optimize import fsolve
import math

port_ret = stock1_cum_ret
def equation(p):
	w1, w2 = p
	return(w1*stock1_cum_ret + w2*stock1_cum_ret - port_ret,np.sqrt((w1**2)*(stock1_variance) + (w2**2)*(stock1_variance) + 2*(w1)*(w2)*(s1s2_cov)))
w1, w2 = fsolve(equation, (0.5,0.5))
print(str((w1/(np.absolute(w1)+np.absolute(w2)))*100) + "%")
print(str((w2/(np.absolute(w1)+np.absolute(w2)))*100) + "%")










