import pandas as pd


#data = {'name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
#        'age': [42, 52, 36, 24, 73],
#        'preTestScore': [4, 24, 31, 2, 3],
#        'postTestScore': [25, 94, 57, 62, 70]}

#df = pd.DataFrame(data, columns = ['name', 'age', 'preTestScore', 'postTestScore'])
# df = pd.read_csv("data.csv", header=None, names=["time","place"])

df = pd.read_csv("data.csv")
print df
print df["time"].describe()
print df["time"].mean()
print df["time"].std()
