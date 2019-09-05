import numpy as np
from collections import Counter


# Instead of using a for loop, let's create a 2D array, each row as a new repetition.
turns = np.random.choice([-1,1],[10,5])
print(turns)   # Individual wins and losses
array = turns.cumsum(axis=1)
print(array)          # This array shows the actual gambling situations.
                      # For each row (repetition), the values of each column
                      # shows the current score. The last column value is the final score.


final_scores = array[:,-1]
print(final_scores)


counts = Counter(final_scores>0)
print('wins',counts[True])
print('loss',counts[False])
print('chances of winning',float(counts[True])/float((counts[True]+counts[False])))

turns = np.random.choice([-1,1],[1000,5])
array = turns.cumsum(axis=1)
final_scores = array[:,-1]
counts = Counter(final_scores>0)
print('wins',counts[True])
print('loss',counts[False])
print('chances of winning',float(counts[True])/float((counts[True]+counts[False])))
