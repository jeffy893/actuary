import pandas


file = open("data.csv","w")

def ineq_bool(alpha, price, rate, wages):
    y = alpha*(price**(1/alpha))*( ((1 - alpha)/rate)**((1 - alpha)/alpha) )
    if(y > wages):
        return True
    else:
        return False

def profit_func(price, alpha, wages, rate, budget, exogenous):
    return (price*(alpha/wages)**alpha)*(((1 - alpha)/(rate))**(1 - alpha))*budget - exogenous

def marginal_revenue(price,alpha,wages,rate):
    return price * ((alpha/wages)**alpha) * (((1 - alpha)/rate)**(1 - alpha))

def highest_profit_with_exogenous():
    p = 100.0
    while(p <= 10000):
        a = 0.05
        while(a < 1):
            w = 10.0
            while(w <= 10000):
                r = 0.5
                b = 10
                while(b <= 10000):
                    ex = 10.0
                    while(ex <= 10000):

                        if(ineq_bool(a,p,r,w)):
                            profit = profit_func(p,a,w,r,b,ex)

                            if(profit > 0):
                                print((str(profit) + "," + str(p) + "," + str(a) + "," + str(w) + "," + str(r) + "," + str(b) + "," +
                                    str(ex) + "\n"))
                                file.write(str(profit) + "," + str(p) + "," + str(a) + "," + str(w) + "," + str(r) + "," + str(b) + "," +
                                    str(ex) + "\n")


                        ex += 100


                    b += 750

                w += 1500

            a += 0.1

        p += 2500


def highest_profit():
    p = 100.0
    while(p <= 10000):
        a = 0.05
        while(a < 1):
            w = 10.0
            while(w <= 10000):
                r = 0.5
                b = 10
                while(b <= 10000):

                    ex = b

                    if(ineq_bool(a,p,r,w)):
                        profit = profit_func(p,a,w,r,b,ex)

                        if(profit > 0):
                            print((str(profit) + "," + str(p) + "," + str(a) + "," + str(w) + "," + str(r) + "," + str(b) + "," +
                                str(ex) + "\n"))
                            file.write(str(profit) + "," + str(p) + "," + str(a) + "," + str(w) + "," + str(r) + "," + str(b) + "," +
                                str(ex) + "\n")



                    b += 100

                w += 500

            a += 0.1

        p += 1000


def highest_profit_wages_per_unit():

    p = 9100.0
    a = 0.05
    w1 = 50.0
    r = 0.5
    b = 9910
    ex = b
    while(w1 <= 500):
        n = 1.0
        while(n <= 10):

            w = w1/n

            if(w >= 0.000000000000000005 and ineq_bool(a,p,r,w1)):
                profit = profit_func(p,a,w,r,b,ex)

                if(profit > 0):
                    print((str(profit) + "," + str(p) + "," + str(a) + "," + str(w1) + "," + str(n) + "," + str(r) + "," +
                        str(b) + "," + str(ex) + "\n"))
                    file.write(str(profit) + "," + str(p) + "," + str(a) + "," + str(w1) + "," + str(n) + "," + str(r) + "," +
                        str(b) + "," + str(ex) + "\n")

            n += 0.25
        w1 += 100





def ambiguous_0_20():
    # a = Alpha
    a = 0.01
    while(a < 1.0):
        # w = Wages
        w = 0.5
        while(w <= 20.0):
            # r = Rental Cost
            r = 0.5
            while(r <= 20.0):
                # p = Price
                p = 0.5
                while(p <= 100.0):

                    mr = marginal_revenue(p,a,w,r)
                    if(mr > 1.0 and mr < 2.0):

                        print((str(mr) + "," + str(p) + "," + str(a) + "," + str(w) + "," + str(r) + "\n"))
                        file.write((str(mr) + "," + str(p) + "," + str(a) + "," + str(w) + "," + str(r) + "\n"))

                    p += 5.0
                r += 1.0
            w += 1.0
        a += 0.05

def ambiguous_20_40():
    # a = Alpha
    a = 0.01
    while(a < 1.0):
        # w = Wages
        w = 20.5
        while(w <= 40.0):
            # r = Rental Cost
            r = 20.5
            while(r <= 40.0):
                # p = Price
                p = 0.5
                while(p <= 300.0):

                    mr = marginal_revenue(p,a,w,r)
                    if(mr > 1.0 and mr < 2.0):

                        print((str(mr) + "," + str(p) + "," + str(a) + "," + str(w) + "," + str(r) + "\n"))
                        file.write((str(mr) + "," + str(p) + "," + str(a) + "," + str(w) + "," + str(r) + "\n"))


                    p += 5.0
                r += 1.0
            w += 1.0
        a += 0.05



# highest_profit()



# highest_profit_wages_per_unit()



# ambiguous_0_20()

ambiguous_20_40()






file.close()
