import numpy as np

A = np.array([[.5,-.5],[-.5,1]])
b = np.array([1,1])
X = np.linalg.solve(A,b)
print 'Expected number of steps from state 0: '+str(X[0])
