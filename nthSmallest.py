"""
Change date format
"""

from datetime import date
import re

def change_date_format(dates):
  dates = str(dates)
  finalList = []
  for date in dates:
    if re.findall(r'(\d{4})/(\d{2})/(\d{2})',date):
      x = re.sub(r'(\d{4})/(\d{2})/(\d{2})', r'\1\2\3',date)
    # a = re.findall(r'\d{4}/\d{2}/\d{2}' ,dates)
    # x = re.sub(a, r'\1\2\3',dates)
      print(x)
      finalList.append(x)

    elif re.findall(r'(\d{2})/(\d{2})/(\d{4})',date):
      x = re.sub(r'(\d{2})/(\d{2})/(\d{4})', r'\3\2\1',date)
      finalList.append(x)

  print (finalList)

dates = change_date_format(["2010/03/30", "15/12/2016"])

#dates = change_date_format(["2010/03/30", "15/12/2016", "11-15-2012", "20130720"])