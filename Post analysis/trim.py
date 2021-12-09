import pandas as pd

df = pd.read_excel('./Excel work/testarw kati bro.xlsx')

# print(df.loc[ df['Avg_O3'].notnull() ])

df_new = df.loc[ df['Avg_O3'].notnull() ]

df_new.to_excel("trimmed_excel.xlsx")