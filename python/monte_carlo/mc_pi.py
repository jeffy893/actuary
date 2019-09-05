import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy.random import random

df = pd.DataFrame({'x':random(1000),'y':random(1000)})

print(df.head())


ax = df.plot(x='x',y='y',kind='scatter')
ax.set_aspect('equal')

plt.show()



df2 = pd.DataFrame()
df2['x'] = 1 - 2 * df['x']
df2['y'] = 1 - 2 * df['y']
ax = df2.plot(x='x',y='y',kind='scatter')
ax.set_aspect('equal')

plt.show()

print(df2.describe())

# The truth values
print((df2['x']**2 + df2['y']**2 < 1).head())



# Now we select these values and make a new dataframe
df_circle = df2[df2['x']**2 + df2['y']**2 < 1]

df_circle.plot(x='x',y='y',kind='scatter')

ax = df_circle.plot(x='x',y='y',kind='scatter')
ax.set_aspect('equal')

plt.show()


print(len(df_circle))
print(len(df2))
print(float(len(df_circle))/float(len(df2)))
print(4 * float(len(df_circle))/float(len(df2)))

df_high = pd.DataFrame({'x':1-2*random(10000),'y':1-2*random(10000)})
print(df_high.head())

df_circle_high = df_high[df_high['x']**2 + df_high['y']**2 < 1]
print(4* float(len(df_circle_high))/float(len(df_high)))

ax = df_circle_high.plot(x='x',y='y',kind='scatter')
ax.set_aspect('equal')

plt.show()
