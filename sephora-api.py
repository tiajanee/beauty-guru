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

# def main():
# 	get_brand()

# '''retrieves the brand name'''
# get_brand():
# url_path = 
req = Request('https://www.sephora.com/new-makeup', headers={'User-Agent': 'Chrome/5.0'})

page = urlopen(req)
soup = BeautifulSoup(page, 'html.parser')
soup.prettify()

# pprint.pprint(soup)
soup.getText()

#EXTRACTING JSON

# spans = (soup.find('div', {"class":"Main-content"}))
# text = spans.findAll('span', {"class": "u-hide"})[1]['data-json']
# json_text = json.loads(text)
# # pprint.pprint(json_text)
# pprint.pprint(json_text['sku_list'])


#EXTRACTING HTML

data = soup.find("span", {"class": "brand"})
if data is not None:
	print("yeer")
# print(data)



# new_text = text.replace("&quot", " ")
# huh_text = new_text.replace("'", "")
# newer_text = new_text.replace(";", "")
# product_list = (newer_text.split("},{"))

# pprint.pprint(product_list)

# print(text)

# sub_soup = BeautifulSoup(str(spans))
# post_soup = sub_soup.findAll("div",{"class":"SkuItem-info"})
# if text is not None:
# 	print("yerr")
# else:
# 	print("nurrr")
# if __name__ == "__main__":
#     main()
