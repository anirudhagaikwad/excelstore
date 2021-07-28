

import pandas as pd

workbook_url = 'https://github.com/anirudhagaikwad/excelstore/blob/main/2018_Sales_Total_Tabs.xlsx'



single_df =  pd.read_excel(workbook_url, sheet_name='Sheet1')


single_df.head()

all_dfs = pd.read_excel(workbook_url, sheet_name=None)
type(all_dfs)
type(all_dfs)
all_dfs.keys()
all_dfs['Sheet1'].head()

all_dfs['Sheet2'].head()

for sheet in all_dfs:
    print(f"{sheet} - {all_dfs[sheet].shape}")

df = pd.concat(all_dfs)

df.shape

df.head()

df.tail()


# Django 
# CherryPy
# TurboGears
# Flask
# Web2Py
# Bottel
# Falcon




