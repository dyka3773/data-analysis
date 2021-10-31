import pandas as pd
from matplotlib import pyplot as plt

field_names = [
                'time', # 0
                'T_in', 'T_out',   #1,2
                'P_in', 'P_out',  #3,5
                'Hum_in', 'Hum_out',   #7,8
                'T_Pump','T_SB',   #9,10
                'Altitude',   #13
                'O3_AE_a', 'O3_WE_a',   #14,15
                'O3_AE_b', 'O3_WE_b',   #16,17
                'CO2_V1_a', 'CO2_V2_a',   #18,19
                'CO2_V1_b', 'CO2_V2_b',   #20,21
                'stage_1'   #36
               ]

cols_to_use = [0,1,2,3,5,7,8,9,10,13,14,15,16,17,18,19,20,21,37]

PATH = './real_data_csv.csv'

df = pd.read_csv(PATH,
                        names = field_names,
                        header = None,
                        usecols = cols_to_use)

# df['time'] = df.apply(lambda x : pd.Timestamp(x['time']//1000, unit = 's'), axis = 1)

#print(df.loc[14022,'time'])
# print(df.head(50))

df_new = df.loc[df['stage_1'] == 1]

# print(df_new.head(50))

# plt.scatter(df_new['time'],df_new['P_in'])
# plt.show()

df_new.to_excel("teliko excelaki.xlsx")