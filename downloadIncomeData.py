import json
import re

import pandas as pd
import requests
from bs4 import BeautifulSoup as bs


def downloadData(web_address, data_name, save_loc):
    r = requests.get(web_address)
    p = re.compile(r'var originalData = (.*);')
    p2 = re.compile(r'datafields:[\s\S]+(\[[\s\S]+?\]),')
    p3 = re.compile(r'\d{4}-\d{2}-\d{2}')
    data = json.loads(p.findall(r.text)[0])
    s = re.sub('\r|\n|\t|\s', '', p2.findall(r.text)[0])
    field_name = p3.findall(s)
    print("The field names are {}".format(field_name))
    field_name.insert(0, 'field_name')  # only headers of interest.
    results = []

    for item in data:  # loop initial list of dictionaries
        row = {}
        for f in field_name:  # loop keys of interest to extract from current dictionary
            if f == 'field_name':  # this is an html value field so needs re-parsing
                soup2 = bs(item[f], 'lxml')
                row[f] = soup2.select_one('a,span').text
            else:
                row[f] = item[f]
        row["field_name"] = row["field_name"].lower().replace(' ', '_').replace('-', '_').strip('"') \
            .replace(',', "_and_").replace("__", "_").replace("(", "").replace(")", "").replace("&", "_and_")
        results.append(row)
    results.append(row)
    df = pd.DataFrame(results)
    df = df.T
    print(df.to_string())
    df.to_csv(r'{location}{file_name}.csv'.format(file_name=data_name, location=save_loc), sep=',',
              encoding='utf-8-sig')


stock_names = [
    "TSLA", "TM", "RIVN", "F", "GM"
]
names = [
    "tesla",
    "toyota",
    "rivian-automotive",
    "ford-motor",
    "general-motors"
]

save_location = "C:/Users/AndyPC/Desktop/ratioData/"
sheets = [
    "balance-sheet", "income-statement", "cash-flow-statement"
]
for stock_name, name in zip(stock_names, names):
    for sheet in sheets:
        url = "https://www.macrotrends.net/stocks/charts/{}/{}/{}".format(stock_name, name, sheet)
        file = name + '-' + sheet
        downloadData(url, file, save_location)
