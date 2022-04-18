from bs4 import BeautifulSoup as bs
import requests, re, json
import pandas as pd

r = requests.get('https://www.macrotrends.net/stocks/charts/TSLA/tesla/income-statement')
p = re.compile(r'var originalData = (.*);')
p2 = re.compile(r'datafields:[\s\S]+(\[[\s\S]+?\]),')
p3 = re.compile(r'\d{4}-\d{2}-\d{2}')
data = json.loads(p.findall(r.text)[0])
s = re.sub('\r|\n|\t|\s','',p2.findall(r.text)[0])
fields = p3.findall(s)
fields.insert(0, 'field_name') # only headers of interest.
results = []

for item in data: #loop initial list of dictionaries
    row = {}
    for f in fields: #loop keys of interest to extract from current dictionary
        if f == 'field_name':  #this is an html value field so needs re-parsing
            soup2 = bs(item[f],'lxml')
            row[f] = soup2.select_one('a,span').text
        else:
            row[f] = item[f]
    results.append(row)

df = pd.DataFrame(results, columns = fields)
print(df)
df.to_csv(r'C:\Users\User\Desktop\Data.csv', sep=',', encoding='utf-8-sig',index = False )