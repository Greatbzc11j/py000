import pandas as pd

df = pd.read_excel("C:\\Users\\land8\\Desktop\\ohlc.xlsx")

df=df.set_index('date')


print(df)