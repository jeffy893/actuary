import scipy as sp

n = float(raw_input('N = '))
iy = float(raw_input('I/Y = '))
pv = float(raw_input('PV = '))
pmt = float(raw_input('PMT = '))
fv = float(raw_input('FV = '))
sol = raw_input('Solve for (n,iy,pv,pmt,fv): ')


if sol == "n":
    print("N = %f" % sp.nper(iy,pmt,pv,fv))
if sol == "iy":
    print("I/Y = %f" % sp.rate(n,pmt,pv,fv))
if sol == "pv":
    print("PV = %f" % sp.pv(iy,n,pmt,fv))
if sol == "pmt":
    print("PMT = %f" % sp.pmt(iy,n,pv,fv))
if sol == "fv":
    print("FV = %f" % sp.fv(iy,n,pmt,pv))




'''
print 'N = %f, ' % n
print 'I/Y = %f, ' % iy
print 'PV = %f, ' % pv
print 'PMT = %f, ' % pmt
print 'FV = %f, ' % fv
'''
