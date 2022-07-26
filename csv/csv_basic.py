import pandas
import numpy as np

L = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

df = pandas.DataFrame(L)
df.to_csv('csv/pandastes.csv')
