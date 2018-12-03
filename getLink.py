#!/Users/ratujareddy/anaconda/bin/python2.7

import requests
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import time 
import sys
import datetime 
from requests.exceptions import ConnectionError
from requests.exceptions import ReadTimeout
from productClass import *

def change_product(product):
	product.link = "hello"
	return product


def get_link(product, store, number_of_attempts=1, new_only=False):
	found = False
	product.link = None
	for _ in range(number_of_attempts):
		try:
			print("trying things")
			r = requests.get(store.shop_url)
			#print(store.shop_url)
			print("ok successfull requested htmp")
			soup = BeautifulSoup(r.content, "lxml", parse_only=SoupStrainer('li'))
			#print(soup)

			print("After soup")
			found_href = False

			# iterating through list of possible
			# categories
			for c_try in product.categories:

				print("Checking: {}".format(c_try))
				category_links = soup.find_all("li", class_=c_try)

				href_list = []

				for item in category_links:
					# check if new item
					# by checking if tag span exists
					if item.span:
						print("Found a new item in category: {}".format(c_try))
						href_list.append(item.find_all("a"))
					else:
						if not new_only:
							print("This is not a new product")
							href_list.append(item.find_all("a"))

				if not href_list:
					#print("Could not find any products in category: {}".format(c_try))
					break

				if href_list:
					full_links = []
					for hrefs in href_list:
						full_links.append(store.base_url+hrefs[0].get("href"))

				for link in full_links:
					r_product = requests.get(link)
					soup_product = BeautifulSoup(r_product.content, "lxml", parse_only=SoupStrainer(["h1", "li"]))
					product_name = str(soup_product.find_all("h1", {"itemprop": "name"})[0].contents[0])
					#print("Looking at: {}".format(product_name))

					if any(x in product_name for x in product.keywords):
						found = True
						#print("FOUND IS TRUE")
						break

				if found:
					startp = time.time()
					print("{} FOUND!".format(product_name))
					#stopp = time.time()
					#timep = stopp-startp
					#print "Time taken to print {} seconds".format(timep)
					style_list = soup_product.find_all('li')

					ptag = [item.find("a", {"data-style-name":True}) for item in style_list if item.find("a", {"data-style-name":True})]

					in_stock = []

					for item in ptag:
						print("ITEM: {}".format(item))
						color = item.get('data-style-name')
						#print("COLOR: {}".format(color))

						sold_out = item.get('data-sold-out')
						if sold_out == "true":
							continue
						else:
							in_stock.append(item)
							if any(x in color for x in product.colors):
								print("{} in stock in {}".format(product_name, color))
								found_href = item.get('href')
								product.link = store.base_url+found_href
								return product

					if product.any_color:
						if in_stock:
							print("\tCould not find desired color but getting available color...\n")
							found_href = in_stock[0].get('href')
							product.link = store.base_url+found_href
							return product
						else:
							return 0
					else:
						return 0
				else:
					return 0

		except (ConnectionError, ReadTimeout):
			time.sleep(1)
			continue

	product.link = None
	return product

#def buy_product(product, store, number_of_attempts=1, new_only=False):
	




