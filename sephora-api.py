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
import requests


# def main():
# 	get_brand()

# '''retrieves the brand name'''
# get_brand():
# url_path = 

headers = {'User-Agent':'Chrome/5.0'}
request = requests.get('https://www.sephora.com/new-makeup', headers=headers,timeout=5)
soup = BeautifulSoup(request.text, 'html5lib')
pprint.pprint(soup)
   
str(soup).replace("&quot;", "")
print(soup)


# results = soup.find_all('meta')
# for result in results:
# if "itemprop" in str(result) and "image" in str(result):
# print(result)



# req = Request('https://www.sephora.com/new-makeup', headers={'User-Agent': 'Chrome/5.0'})
# page = urlopen(req)
# soup = BeautifulSoup(page, 'html.parser')
# soup.prettify()



# # pprint.pprint(soup)

# #EXTRACTING JSON

# #EXTRACTING HTML

# containers =  soup.find("div", {"class":"Main-content"})
# div = containers.find('div', {"class":"SkuGrid.ng-scope"})
# print(div)
# # pprint.pprint(containers.)

# a = containers.findAll('div', attrs={"seph-sku-item"})
# print(a)
# for az in a:
# 	pprint.pprint(a)
#concatenates extensions to base link, aggregates the new product links into a list

	# if prod_link:
	# 	prod_href = str(prod_link.get('href'))
	# 	print(prod_href)
		#link compositions vary, if-statement accounts for edge case
		# if prod_href[0] != 'h':
		# 	prod_href = 'https://www.ulta.com' + prod_href
		# nav_to_links.append(prod_href)

