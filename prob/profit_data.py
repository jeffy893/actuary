import numpy as np
import csv


file1 = open("profit1.csv","w")
file2 = open("profit2.csv","w")
file3 = open("profit3.csv","w")
file4 = open("profit4.csv","w")

count = 1
trig = 1

r = 10.0


def profit(alpha, omega, ar, pg, bf, zeta):
    return pg *  ( (alpha * (bf - zeta))/(omega) )**alpha * ( ( (bf - zeta)*(1 - alpha) )/(ar) )**(1 - alpha) - bf

a = 0.05
while(a <= 1.0):
    w = 10.0
    while(w <= 10000.0):
        p = 10.0
        while(p <= 10000.0):
            b = 10.0
            while(b <= 10000.0):
                z = 5.0
                while(z < b):
                    r = (w * (1.0 - a))/(a)
                    prof = profit(a,w,r,p,b,z)
                    print(str(prof) + "," + str(a) + "," + str(w) + "," + str(r) + "," + str(p) + "," + str(b) + "," + str(z))
                    text = str(prof) + "," + str(a) + "," + str(w) + "," + str(r) + "," + str(p) + "," + str(b) + "," + str(z)
                    if(prof > 0):
                        if(trig == 1):
                            file1.write(text + "\n")
                        if(trig == 2):
                            file2.write(text + "\n")
                        if(trig == 3):
                            file3.write(text + "\n")
                        if(trig == 4):
                            file4.write(text + "\n")
                        if(count == 1000000):
                            count = 1
                            trig += 1
                        count += 1

                    z += 50.0
                b += 250.0
            p += 500.0
        w += 750.0
    a += 0.15


file1.close()
file2.close()
file3.close()
file4.close()
