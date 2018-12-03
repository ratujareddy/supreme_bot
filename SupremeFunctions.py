#!/Users/ratujareddy/anaconda/bin/python2.7

from splinter import Browser
from selenium import webdriver
import time

def fill_billing_info(browser, User):
	browser.fill('order[billing_name]', User.billing.name)
	browser.fill('order[email]', User.billing.email)
	browser.fill('order[tel]', User.billing.phone)
	browser.fill('order[billing_address]', User.billing.address)
	browser.fill('order[billing_zip]', User.billing.zipcode)
	browser.fill('order[billing_city]', User.billing.city)

def fill_card_info(browser,User):
	#browser.find_option_by_text(User.card.ctype).first.click() #American Express #Visa
	browser.fill('credit_card[nlb]', User.card.number)
	browser.find_option_by_text(User.card.exp_month).first.click() #01-12
	browser.find_option_by_text(User.card.exp_yr).first.click() #2016 - 2026
	browser.fill('credit_card[rvv]', User.card.cvv)

def buy_product(product, store, buyer):
	chrome_options = webdriver.ChromeOptions()
	prefs = {"profile.managed_default_content_settings.images":2}
	chrome_options.add_argument('--disable-extensions')
	chrome_options.add_experimental_option("prefs",prefs)
	#chrome_options.Proxy = null
	#browser = Browser('chrome')
	browser = Browser('chrome', chrome_options)
	#browser.driver.set_window_size(1234, 987)
	#browser = webdriver.Chrome()
	#browser = webdriver.Chrome("/usr/local/bin/chromedriver")
	browser.visit(product.link)
	#print("finding size")

	foundsize = False
	for size in product.sizes:
		#print("looking for size: {}".format(size))
		size_button = browser.find_by_text(size)
		if size_button:
			foundsize = True
			#print("found size: {}".format(size))
			size_button.click()
			break

	if not foundsize:
		if product.any_size:
			print("\tCould not find desired size, but getting available size...")
		else:
			return 0
	try:
		add_to_cart = browser.find_by_name('commit')
		add_to_cart.click()
	except (AttributeError):
		print("Product seems to be sold out")
		return 0

	time.sleep(0.1)
	browser.visit(store.checkout_url)
	fill_billing_info(browser, buyer)
	fill_card_info(browser, buyer)

	browser.find_by_css('.terms').click()
	browser.find_by_name('commit').click()
	return 1



