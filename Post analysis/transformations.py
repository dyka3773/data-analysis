import pandas as pd

tsv1 = pd.read_csv("New Text Document.txt", sep='\t')

tsv1.to_excel("BX30_Esrange_20210930_045350_EDT_PTULevels.xlsx")