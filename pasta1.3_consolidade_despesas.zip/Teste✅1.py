import pandas as pd

df1 = pd.read_csv('1T2025.csv', sep=';')
df2 = pd.read_csv('2T2025.csv', sep=';')
df3 = pd.read_csv('3T2025.csv', sep=';')

df = pd.concat([df1, df2, df3])