

from bs4 import BeautifulSoup
import urllib.request
import os

html = urllib.request.urlopen("https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India")

soup = BeautifulSoup(html, "html.parser")

theClass = soup.find_all("table", {"class": "vertical-navbox nowraplinks"})

for tr in theClass:
    print(tr)
    for th in tr:
        print(th)
