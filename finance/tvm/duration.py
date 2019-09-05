import scipy as sp
import numpy as np
import csv
import matplotlib.pyplot as plt

# independent variable for plots
x = np.linspace(0, 0.12, 256, endpoint = True)


print("Looking for CSV with the following format:\n")
print("[CF0.0]:[t0.1],[CF0.2]:[t0.2],...\n")
print("[CF1.0]:[t1.1],[CF1.2]:[t1.2],...\n")
print("[CF2.0]:[t2.1],[CF2.2]:[t2.2],...\n")


file = raw_input('Name of CSV File = ')
iy = float(raw_input("Interest Rate = "))


with open(file) as csv_file:
    cash_flows = csv.reader(csv_file, delimiter=',')
    row_count = 1
    for row in cash_flows:


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

        print("The Present Value of Row %d is %f" % (row_count,pv_row))
        print("The MaCaulay Duration of Row %d is %f" % (row_count,duration))
        # print("The Temp Duration of Row %d is %f" % (row_count,dur_temp))

        plt.figure()
        plt.plot(x, plot_dur, '-g', label=r'Temp')




        row_count += 1
    plt.show()
