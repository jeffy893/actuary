import math
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

array = np.random.choice([-1,1],10000)
print(array[:10])
plt.plot(array[:10].cumsum(),'go')
plt.show()

counts = Counter(array)
print('Total Heads',counts[1])
print('Total Tails',counts[-1])
print('Final value',array.cumsum()[-1])
print('Probability of Heads', float(counts[1])/float(array.size))
print('Probability of Tails', float(counts[-1])/float(array.size))
