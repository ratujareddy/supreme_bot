#!/Users/ratujareddy/anaconda/bin/python2.7

from productClass import *
from SupremeFunctions import *
from getLink import *
from splinter import Browser
import sys
import datetime 
import os

#os.nice(10)

def main():

	# import splinter
	# print("SPLINTER VERSION:")
	# print splinter.__version__

	start_time = time.time()
	mydate = datetime.datetime.now()
	print "Running " + str(sys.argv[0]) + " on " + mydate.strftime("%B %d, %Y at %I:%M %p") + "\n"

	f = open("thisworkssss.txt", 'w')

	reload(sys)
	#print("SYS")
	#print sys.path
	sys.setdefaultencoding('utf-8')
	supreme = StoreSite("SupremeClothing", "http://www.supremenewyork.com")
	supreme.shop_url = "http://www.supremenewyork.com/shop"
	supreme.checkout_url = "http://www.supremenewyork.com/checkout"

	home = BillingInfo("Ratuja Reddy", "ratuja@gmail.com", "789879879", "5555 S Main St", "Chicago", "60615")
	debit = CardInfo("Mastercard", "5555222255559999", "03", "2020", "100")
	ratuja = Buyer("Ratuja", home, debit)
 
	# arrow shirt
	arrow = Product("T-Shirt")
	arrow.categories = ["accessories"]
	arrow.keywords = ["Tagless"]
	arrow.colors = [""]
	arrow.sizes = ["Small"]
	arrow.any_color = True

	# flannel
	flannel = Product("Flannel Shirt")
	flannel.categories = ["shirts"]
	flannel.keywords = ["a;lskdjf"]
	flannel.colors = ["Pink", "pink"]
	flannel.sizes = ["Medium"]
	flannel.any_color = True

	# hat
	hat = Product("Logo Hat")
	hat.categories = ["hats"]
	hat.keywords = ["Vertical"]
	hat.colors = ["Pink", "pink"]
	hat.sizes = ["Medium"]
	hat.any_color = True

	ratuja.first_choice = arrow
	ratuja.second_choice = flannel
	ratuja.third_choice = hat

	all_choices = [ratuja.first_choice, ratuja.second_choice, ratuja.third_choice]

	t_end = time.time() + 60 * 0.2
	while time.time() < t_end:
	#for _ in range(5):
		for product in all_choices:
			print("\nLOOKING FOR: {}\n".format(product.name))
			get_link(product, supreme)

			if product.link:
				print("\nTotal Time To Get Link %s\n" % (time.time() - start_time))
				print("\tFound link to: {}\n".format(product.name))
				print("Link is: {}".format(product.link))

			else:
				print("\tSorry, could not get a link for {}".format(product.name)) 
				continue

			rv = buy_product(product, supreme, ratuja)
			if rv == 1:
				print("\n\tSuccessfully purchased {}!".format(product.name))
				print("\n\tTotal Time To Purchase is %s seconds\n" % (time.time() - start_time))
				return
			
			if rv == 0:
				print("\n\tFound link, but could not purchase {}.".format(product.name))
				continue 
		

	f.write("I worked!!!")
	print("\nTotal Time Without Purchase %s\n" % (time.time() - start_time))
	
if __name__ == "__main__":
    main()









    
