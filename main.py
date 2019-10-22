import pandas as pd

data = {'0': [1, 0, 1, 0, 0], '1': [1, 1, 1, 1, 1], '2': [2, 2, 2, 2, 2]}
df = pd.DataFrame(data)
print(df.ix[:, (df != df.ix[0]).any()])