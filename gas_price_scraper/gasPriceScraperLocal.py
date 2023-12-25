from bs4 import BeautifulSoup
from nbformat import write
from pytz import country_names
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

megaAddress = []

count = 0
names = []
prices = []
locations = []
batchSize = 1000

data = pd.read_excel ('localLinks.xlsx')
dataCol1 = data['Local Links']
dataCol2 = data ['Local Names']
localLinks = []
localName = []
index = pd.read_excel ('IndexLocal.xlsx')
index = index ['Index']
index = index[0]
index = (int)(index)

for i in range (index, index+batchSize):
    localLinks.append (dataCol1[i])
for i in range (index, index+batchSize):
    localName.append (dataCol2[i])

for url in localLinks:
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    

    for thing in soup.find_all ('div', class_='StationDisplay-module__mainInfoColumn___1ZBwz StationDisplay-module__column___3h4Wf'):
        names.append (thing.h3.a.text)
        # print (thing.h3.a.text)

    

    for thing in soup.find_all ("span",class_="StationDisplayPrice-module__price___3rARL"):
        prices.append (thing.text)
        # print (thing.text)

    

    for thing in soup.find_all ('div', class_='StationDisplay-module__address___2_c7v'):
        location = ""
        location += thing.text
        locations.append (location + ";" + localName[count])
        # print (location)
    

    count+=1
    # print (names)
    # print (prices)
    # print (locations)

for i in range (len(locations)):
    megaAddress.append (names[i] + ';' + locations[i])


currData = np.array (pd.read_excel ('FinalData.xlsx'))
print (currData)
currDataArrAddress = []
currDataArrPrices = []
for i in range (len(currData)):
    currDataArrAddress.append (currData[i][0])
    currDataArrPrices.append (currData[i][1])

if currData.size>0:
    for i in range (len(megaAddress)):
        currDataArrAddress.append (megaAddress[i])
        currDataArrPrices.append(prices[i])
else:
    currDataArrAddress = megaAddress
    currDataArrPrices = prices
pushingFinalData = {"Mega Address":currDataArrAddress,
                 "Price":currDataArrPrices}
df = pd.DataFrame (pushingFinalData, columns = ['Mega Address', 'Price'])
# writingData = pd.concat ([currData, df], axis = 1)
df.to_excel (r'C:\Users\kavis\Desktop\KAVISH\General Stuff\Gas Prices Project\FinalDataLocal.xlsx', index = False, header=False)
indexArr = {"Index":(index+batchSize)}

dfIndex = pd.DataFrame (indexArr, columns=['Index'], index={0})
dfIndex.to_excel (r'C:\Users\kavis\Desktop\KAVISH\General Stuff\Gas Prices Project\IndexLocal.xlsx', index = False, header=True)

print (megaAddress)
print (prices)




# Epic Roshan Code
# rows = []
# f = open("data.csv", "w")
# name = ' '.join(str(e) for e in names)
# price = ' '.join(str(e) for e in prices)
# f.write("1. " + name +"\n")
# f.write("1. " + price)
# f.close()

