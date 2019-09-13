import scipy as sp
import numpy as np
import csv
import matplotlib.pyplot as plt

# independent variable for plots
x = np.linspace(0, 0.12, 256, endpoint = True)


print("Looking for CSV with the following format:\n")
print("Cash Flows and Time as Float:\n")
print("CF0,CF1,CF2,...\n")
print("t0,t1,t2,...\n")


file = raw_input('Name of CSV File with Extension = ')
iy = float(raw_input("Float Interest Rate = "))


with open(file) as csv_file:
    raw = csv.reader(csv_file, delimiter=',')

    raw_list = list(raw)

    cf_count = 0

    for cf_row in raw_list[0]:
        cf_count += 1

    row = []

    for i in range(0,cf_count):
        row.append(raw_list[0][i] + ":" + raw_list[1][i])

    '''
    for temp in row:
        print(temp)
    '''

    pv_row = 0.0
    pv_prime_row = 0.0

    plot_row = 0.0
    plot_prime_row = 0.0
    # temp_pv_row = 0.0

    for cash_time in row:
        ct = cash_time.split(":")
        cash = float(ct[0])
        time = float(ct[1])
        # print("Cash Flow %f at Time %f\n" % (cash, time))

        # Current Present Value
        pv_now = cash*(1 + iy)**(-1 * time)
        plot_now = cash*(1 + x)**(-1 * time)

        pv_prime_now = (cash*time)*(1 + iy)**(-1 * (time+1))
        plot_prime_now = (cash*time)*(1 + x)**(-1 * (time+1))

        # temp_pv_now = (cash*time)*(1 + iy)**(-1 * time)
        pv_row = pv_row + pv_now
        pv_prime_row = pv_prime_row + pv_prime_now

        plot_row = plot_row + plot_now
        plot_prime_row = plot_prime_row + plot_prime_now
        # temp_pv_row = temp_pv_row + temp_pv_now

    duration = (1 + iy)*(pv_prime_row/pv_row)
    plot_dur = (1 + x)*(plot_prime_row/plot_row)
    # dur_temp = temp_pv_row/pv_row

    print("The Present Value is %f" % pv_row)
    print("The MaCaulay Duration %f" % duration)
    # print("The Temp Duration of Row %d is %f" % (row_count,dur_temp))

    plt.figure()
    plt.plot(x, plot_dur, '-g', label=r'Temp')



    plt.show()
