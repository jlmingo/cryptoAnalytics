import requests
from bs4 import BeautifulSoup
import pandas as pd

#This file gets gold prices from https://www.usagold.com/
#For 2019, data can be retrieved with regular scrapping
#For years 2018 to 2014, selenium must be used

##Retrieving 2019 gold prices

url = "https://www.usagold.com/reference/prices/goldhistory.php"

#Setting fake user-agent to avoid anti-scrapping in selected web
#Retrieving quotes and dates from 2019 table

HDR = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
res = requests.get(url, headers=HDR)
html = res.text
soup = BeautifulSoup(html, 'html.parser')
quotes = soup.select('#quotes tr td')

##Creating DataFrame from information retrieved

quoteDate = [e.text for e in quotes[1:]]

d = {
    
    "Date": [e for e in quoteDate if quoteDate.index(e) % 2 == 0],
    "Quote": [e for e in quoteDate if quoteDate.index(e) % 2 != 0]
}

df = pd.DataFrame(d)

#Setting Date's format as DateTime; setting column as index

df['Date']= pd.to_datetime(df['Date'])
df.set_index("Date", inplace=True)

##Retrieving 2014-2018 gold prices (selenium needed) - Work in progress
