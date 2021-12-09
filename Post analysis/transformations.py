import pandas as pd
import csv

FILENAME = "C:/Users/HerculesKonsoulas/OneDrive/Random Stuff/Programming_Random/Δημήτρης/NASA's data.tsv"
CSV_FILENAME = "./Nasa's data.csv"
DEST_FILENAME = "./Nasa's data.xlsx"

# tsv1 = pd.read_csv(FILENAME, sep='\t', header=None)

# # print(tsv1)

# list =[]

# for line in tsv1.loc[:,0]:
#     list.append(line.split())


# # print(list)

# with open(CSV_FILENAME, 'w', newline='') as f:
      
#     # using csv.writer method from CSV package
#     write = csv.writer(f)

#     string = "ElapTime(s) Press(hPa) GeopHgt(m) Temp(K)  RH(%)   PO3(mPa)    DD(degE)    FF(m/s)  GPSHgt(m)     Lon(degE)     Lat(degN)   PmpT(K)     Ozi(uA)  Vpmp(V)    Ipmp(mA)"

#     write.writerow(string.split())

#     for listItem in list:
#         write.writerow(listItem)
    
""" UNCOMMENT ONE PART AT A TIME """

# csv = pd.read_csv(CSV_FILENAME)

# # print(csv)

# csv.to_excel(DEST_FILENAME)