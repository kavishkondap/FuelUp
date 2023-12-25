from distutils.filelist import findall
from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd
import xlrd
from lxml import etree
from openpyxl import Workbook, load_workbook
import numpy as np

data = pd.read_excel('states.xlsx')
states = data['LowerState']
stateLinks = []

for i in range (50):
    if ' ' in states[i]:
        correctFormatting = states[i][0:states[i].index(' ')] + '-' + states[i][states[i].index(' ')+1:]
        states[i] = correctFormatting
    stateLinks.append ("https://www.gasbuddy.com/gasprices/" + states[i])

print (stateLinks)

for url in stateLinks:
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    for thing in soup.find_all ('div', class_='grid__column___nhz7X grid__mobile6___3PWzR grid__tablet4___3sPs8 DataGrid-module__gridEntry___1Ivee AreaCountyList-module__areaItem___3c4w7'):
        link = thing.a['href']
        link = "https://www.gasbuddy.com/" + link
        print (link)