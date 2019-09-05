import rpy2.robjects as robj
from rpy2.robjects.packages import importr
base = importr('base')
stats = importr('stats')

data = robj.vectors.DataFrame.from_csvfile("data.csv", header=True, sep=',')
Y = data[1]
X = data[0]
fmla = robj.Formula("Y ~ X")
env = fmla.environment
env['X'] = X
env['Y'] = Y


fit = stats.lm(fmla)


print(base.sumary(fit))

