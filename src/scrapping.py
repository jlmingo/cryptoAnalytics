import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import re
import os

#This file gets gold prices from https://www.usagold.com/
#For 2019, data can be retrieved with regular scrapping
#For years 2014 to 2018, selenium must be used

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

df_2019 = pd.DataFrame(d)

#Setting Date's format as DateTime; setting column as index

df_2019['Date']= pd.to_datetime(df_2019['Date'])
df_2019.set_index("Date", inplace=True)

##Retrieving 2014-2018 gold prices (selenium needed) - Work in progress

# website urls
base = "https://www.usagold.com/reference/prices/goldhistory.php"

#Firefox session
driver = webdriver.Firefox()
driver.get(base)
driver.implicitly_wait(100)

#Selects gold daily quotes from years a to b (excluding b)
def goldHistorics(a,b):
    quote_gold = []
    for i in range(a, b):
        button = driver.find_element_by_id("goldpricemenu")
        button.click()
        button = driver.find_element_by_css_selector('a[href*="{}"]'.format(i))
        button.click()
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        quote_gold.append(soup.select('#quotes tr td'))

    print("Selection finished")
    return quote_gold

quote_gold = goldHistorics(2014, 2019)

quote_gold_clean = [i.text for e in quote_gold for i in e[1:]]
quote_gold_clean
d = {
    "Date": [e for e in quote_gold_clean if quote_gold_clean.index(e) % 2 == 0],
    "Quote": [e for e in quote_gold_clean if quote_gold_clean.index(e) % 2 != 0]
}
df_historical = pd.DataFrame(d)

df_historical['Date']= pd.to_datetime(df_historical['Date'])
df_historical.set_index("Date", inplace=True)

#Concatenating all data in one
df = df_2019.append(df_historical)
df.fillna(method='ffill')
df.to_csv("gold_quotes_historical.csv")
print("Gold quotes historical csv file generated")