from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/Lists_of_stars"

options=webdriver.ChromeOptions()
browser = webdriver.Chrome(options=options)
browser.get(START_URL)

scraped_data=[]

def scrape():
    soup=BeautifulSoup(browser.page_source,'html.parser')
    bright_table=soup.find('table',attrs={'class','wikitable'})
    table_body=bright_table.find('tbody')
    table_row=table_body.find_all('tr')
    for row in table_row:
        table_col=row.find_all('td')
        temp_list=[]
        for col_data in table_col:
            data=col_data.text.strip()
            temp_list.append(data)
        scraped_data.append(temp_list)
    

scrape=()

stars_data=[]

for i in range(0,len(scraped_data)):

    Star_names= scraped_data[i][1]
    Distance = scraped_data[i][3]
    Mass = scraped_data[i][5]
    Radius = scraped_data[i][6]
    Lum = scraped_data[i][7]

    required_data=[Star_names,Distance,Mass,Radius,Lum]
    stars_data.append(required_data)


print(stars_data)

headers=['Star_names','Distance','Mass','Radius','Lum']

star_df_1=pd.DataFrame(stars_data, columns=headers)

star_df_1.to_csv('scraped_data', index=True, index_label='id')

