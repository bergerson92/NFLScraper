import requests
from bs4 import BeautifulSoup
import pandas as pd
import pygsheets

response = requests.get(
    url="https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions"
)

# print(response.status_code)

soup = BeautifulSoup(response.content, "html.parser")

# title = soup.find(id="firstHeading")

# print(title.string)

championstable = soup.find("table", {"class": "wikitable sortable"})

# print(championstable)

df = pd.read_html(str(championstable))
df = pd.DataFrame(df[0])
# print(df)

gc = pygsheets.authorize(
    service_file="/Users/pathtoFile"
)

# df = pd.DataFrame()

# df['name'] = ['John', 'Sarah', 'Steve']

sh = gc.open("NFL Champions")

wks = sh[0]

wks.set_dataframe(df, (1, 1))
