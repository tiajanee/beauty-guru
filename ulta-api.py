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


BASE_URL = 'https://www.ulta.com/new-beauty-products?N=6Z26y1&No='

NEWPROD_PAGE_LINKS = ['0&Nrpp=96', '96&Nrpp=96', '192&Nrpp=96', '288&Nrpp=96', '384&Nrpp=96']
page_count = 0
while page_count < len(NEWPROD_PAGE_LINKS):

	req = Request(BASE_URL+NEWPROD_PAGE_LINKS[page_count], headers={'User-Agent': 'Chrome/5.0'})

	page = urlopen(req)
	soup = BeautifulSoup(page, 'html.parser')
	soup.prettify()

	#scrapes new product links
	prod_title = soup.findAll('h4', 'prod-title')

	nav_to_links = []

	#concatenates extensions to base link, aggregates the new product links into a list
	for title in prod_title:
		prod_link = title.find('a', href=True)
		if prod_link:
			prod_href = str(prod_link.get('href'))
			#link compositions vary, if-statement accounts for edge case
			if prod_href[0] != 'h':
				prod_href = 'https://www.ulta.com' + prod_href
			nav_to_links.append(prod_href)

	#variable that increments to parse all the links
	n = 0
	for link in nav_to_links:
		print(link)
		new_req = Request(nav_to_links[n])
		new_page = urlopen(new_req)
		new_soup = BeautifulSoup(new_page, 'html.parser')

		#scrapes script tag for JSON data
		text = new_soup.find('script', {'type':'application/ld+json'})
		json_text = json.loads(text.getText())

		#extracts relevant product information
		product_title = json_text['name']
		product_brand = json_text['brand']
		product_price = json_text['offers']['price']
		print(product_title, product_brand, '$'+ product_price)
		
		if n < len(nav_to_links):
			n += 1
	page_count += 1

