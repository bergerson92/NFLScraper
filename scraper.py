import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get(url="https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions")

#print(response.status_code)

soup = BeautifulSoup(response.content, 'html.parser')

title = soup.find(id="firstHeading")

#print(title.string)

championstable = soup.find('table', {'class':"wikitable sortable"})

#print(championstable)

df = pd.read_html(str(championstable))
df=pd.DataFrame(df[0])
#print(df)

