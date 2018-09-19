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

#EXTRACTING JSON

# spans = (soup.find('div', {"class":"Main-content"}))
# text = spans.findAll('span', {"class": "u-hide"})[1]['data-json']
# json_text = json.loads(text)
# # pprint.pprint(json_text)
# pprint.pprint(json_text['sku_list'])


#EXTRACTING HTML
lol = soup.find('a')
print(lol)
	# if lol is not None:
	# 	for laugh in lol:
	# 		a = laugh.find('a')
	# 		print(a)
# print(data)
# if data is not None:
# 	for title in data:
# 		prod_link = title.find('a', href=True)
# 		print(prod_link)
# # print(data)
# nav_to_links = []

#concatenates extensions to base link, aggregates the new product links into a list

	# if prod_link:
	# 	prod_href = str(prod_link.get('href'))
	# 	print(prod_href)
		#link compositions vary, if-statement accounts for edge case
		# if prod_href[0] != 'h':
		# 	prod_href = 'https://www.ulta.com' + prod_href
		# nav_to_links.append(prod_href)

