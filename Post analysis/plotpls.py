import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_excel('testarw kati bro.xlsx')

# print(df)

plt.scatter(df['time'],df['P_in'])
plt.show()