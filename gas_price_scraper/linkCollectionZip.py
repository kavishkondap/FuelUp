import requests
import pandas as pd


data = pd.read_excel('countyLinks.xlsx')
countyLinks = data['County Links']

zipLinks = []
zipNames = []

for i in range (100000):
    try:
        s = requests.Session()
        s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        s.max_redirects = 9223372036854775807
        url = 'https://www.gasbuddy.com/home?search=' + str (i)
        page = s.get(url)
        zipLinks.append (url)
        zipNames.append (i)
        print (url)
    except:
        pass

pushingData = {"Zip Links":zipLinks,
                "Zip Names":zipNames}
df = pd.DataFrame (pushingData, columns = ['Zip Links', 'Zip Names'])

df.to_excel (r'C:\Users\kavis\Desktop\KAVISH\General Stuff\Gas Prices Project\zipLinks.xlsx', index = False, header=True)