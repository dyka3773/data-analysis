import pandas as pd
import csv

tsv1 = pd.read_csv("testing.csv")

# print(tsv1)

# list =[]

# for line in tsv1.loc[:,0]:
#     list.append(line.split())


# # print(list)

# with open('testing.csv', 'w', newline='') as f:
      
#     # using csv.writer method from CSV package
#     write = csv.writer(f)

#     string = " min  s      hPa      gpm     deg_C      hum  deg_C  Automatic  Operator  flag1   flag2"

#     write.writerow(string.split())

#     for listItem in list:
#         write.writerow(listItem)
    

tsv1.to_excel("BX31_Esrange_20210929_071127_EDT_PTULevels.xlsx")