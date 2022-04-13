# import openpyxl
from cmath import log
from traceback import print_tb
import pandas as pd
# import numpy as np

# excelFile = 'C:/Users/eurobit/Desktop/olx/ekifJan.xlsx'
KIF = 'C:/Users/eurobit/Desktop/olx/KIF_MICRO.xlsx'

values = []

df = pd.read_excel(KIF, sheet_name='KIF')
# for date in df.datum:
#   if(pd.Timestamp(date) > pd.Timestamp(2022,3,1)):
#     print(pd.Timestamp(date))
# df.query('`Mjesto dostave`.pd.Timestamp(2022,3,1)')

kupci = df['Mjesto dostave'].where(pd.Timestamp(df['datum']) > pd.Timestamp(2022,3,1))
print(kupci)

# dates = df['datum'].where(df['sjediste'] == 'Sarajevo')
# print(df['datum'], pd.Timestamp(2021,1,10))
# dates = pd.Timestamp(df.datum) > pd.Timestamp(2021,1,10),

  # print(pd.Timestamp(date) > pd.Timestamp(2021,1,10))
  # if(date <= pd.Timestamp(2021,1,10)):
  #   print(date)
# print(dates.dropna())
# print(pd.Timestamp(2020,1,10))
# print(df.datum)


# df.newest_date_available < pd.Timestamp(2016,1,10)




# for file in excelFiles:
# # print(excelFile)
# workbook = openpyxl.load_workbook(KIF, read_only=True)
# kifSheet = workbook['KIF']
# # print('kifSheet ', kifSheet)

# for row in kifSheet.iter_rows("H"):
#   # print('row', row)
#   for cell in row:
#     print('cell', cell)
# # cell_value = worksheet['B12'].value
# # values.append(cell_value)
# # print(cell_value)

