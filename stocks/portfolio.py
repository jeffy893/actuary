import numpy as np
import csv

print("\n")

numStocks = int(raw_input('How many stocks do you want to use?  '))

for j in range(numStocks):
	exec("stockName" + str(j) + " = raw_input('What is the name of stock " + str(j) + "?  ')")

print("\n")

for i in range(numStocks):
	exec("stock" + str(i) + " = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]\ncount = 0\nwith open('stock" + str(i) + ".csv', 'rb') as csvfile:\n\tread = csv.reader(csvfile, delimiter=',')\n\tfor row in read:\n\t\t#if(count > 0):\n\t\tstock" + str(i) + "[count] = float(row[1])\n\t\t#print row[0] + ',' + row[1]\n\t\tcount += 1\n\tcount = 0\nstock" + str(i) + "_returns = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]\nfor count in range(12):\n\tif(count < 11):\n\t\tstock" + str(i) + "_returns[count] = (stock" + str(i) + "[count+1] - stock" + str(i) + "[count])/stock" + str(i) + "[count]\nstock" + str(i) + "_cum_ret = 0.0\nfor count in range(11):\n\tstock" + str(i) + "_cum_ret += stock" + str(i) + "_returns[count]\nstock" + str(i) + "_avg_daily_ret = stock" + str(i) + "_cum_ret / 10.0\nstock" + str(i) + "_sum_squared_error = 0.0\nfor count in range(11):\n\tstock" + str(i) + "_sum_squared_error += ((stock" + str(i) + "_returns[count] - stock" + str(i) + "_avg_daily_ret)**2)\nstock" + str(i) + "_variance = stock" + str(i) + "_sum_squared_error/10.0\nstock" + str(i) + "_standard_deviation = np.sqrt(stock" + str(i) + "_variance)")



# Portfolio Return
#port_ret = w1*r1 + w2*r2 + ... + wn*rn
#port_ret = w1*stock1_cum_ret + w2*stock2_cum_ret
# Portfolio Variance
#port_var = (w1**2)*(stock1_variance) + (w2**2)*(stock2_variance) + 2*(w1)*(w2)*(s1s2_cov)



for i in range(numStocks - 1):
	exec("squared_error = 0.0\nfor count in range(11):\n\tsquared_error += (stock" + str(i) + "_returns[count] - stock" + str(i) + "_avg_daily_ret)*(stock" + str(i) + "_returns[count] - stock" + str(i) + "_avg_daily_ret)\ns" + str(i) + "s" + str(i + 1) + "_cov = squared_error / 10.0\nsquared_error = 0.0")



from scipy.optimize import fsolve
import math

for i in range(numStocks - 1):
	exec("s" + str(i) + "s" + str(i + 1) + "port_ret = stock" + str(i) + "_cum_ret + stock" + str(i + 1) + "_cum_ret\ndef equation(p):\n\tw1, w2 = p\n\treturn(w1*stock" + str(i) + "_cum_ret + w2*stock" + str(i + 1) + "_cum_ret - s" + str(i) + "s" + str(i + 1) + "port_ret,(w1**2)*(stock" + str(i) + "_variance) + (w2**2)*(stock" + str(i + 1) + "_variance) + 2*(w1)*(w2)*(s" + str(i) + "s" + str(i + 1) + "_cov))\ns" + str(i) + "s" + str(i + 1) + "w1, s" + str(i) + "s" + str(i + 1) + "w2 = fsolve(equation, (1 / numStocks,1 / numStocks))")


for i in range(numStocks - 1):
	exec("group" + str(i) + "w1 = (s" + str(i) + "s" + str(i + 1) + "w1/(np.absolute(s" + str(i) + "s" + str(i + 1) + "w1)+np.absolute(s" + str(i) + "s" + str(i+1) + "w2)))\ngroup" + str(i) + "w2 = (s" + str(i) + "s" + str(i + 1) + "w2/(np.absolute(s" + str(i) + "s" + str(i + 1) + "w1)+np.absolute(s" + str(i)  + "s" + str(i+1) + "w2)))\ns" + str(i) + "s" + str(i + 1) + "mult = group" + str(i) + "w2 / group" + str(i) + "w1")

finalWeight0 = 100.0
for i in range(numStocks):
	if(i > 0):
		exec("finalWeight" + str(i) + " = s" + str(i-1) + "s" + str(i) + "mult * finalWeight" + str(i - 1) +"")


totalFinalWeight = 0.0
for i in range(numStocks):
	exec("totalFinalWeight += np.absolute(finalWeight" + str(i) + ")")

port_cum_ret = 0.0
for i in range(numStocks):
	exec("port_cum_ret += stock" + str(i) + "_cum_ret")

print('Portfolio Return = ' + str(port_cum_ret/numStocks))

for i in range(numStocks):
	exec("print(stockName" + str(i) + ")\nprint('Return = ' + str(stock" + str(i) + "_cum_ret))\nprint('Standard Deviation = ' + str(stock" + str(i) + "_standard_deviation))\nprint('Weight = ' + str((finalWeight" + str(i) + " / totalFinalWeight)*100) + '  %')")
