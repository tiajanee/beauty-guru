import re
import csv
import glob
import pprint
import httplib2
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup, SoupStrainer
import os
import json


req = Request('https://www.sephora.com/new-makeup', headers={'User-Agent': 'Chrome/5.0'})

page = urlopen(req)
soup = BeautifulSoup(page, 'html.parser')
soup.prettify()

# pprint.pprint(soup)
# soup.getText()
# print(soup)

data = soup.find('div', {"class": "productQvContainer"})
if data is not None:
	print("Yeer")
else:
	print("nurr")