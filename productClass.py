#!/Users/ratujareddy/anaconda/bin/python2.7

class StoreSite(object):

    def __init__(self, name, base_url):
        self.name = name
        self.base_url = base_url
        self.shop_url = None
        self.checkout_url = None

    def __repr__(self):
        return "{}: {}".format(self.name, self.base_url)


class Product(object):
    PRODUCT_TRY = 0

    def __init__(self, name):
        Product.PRODUCT_TRY += 1
        self.ptry = Product.PRODUCT_TRY
        self.name = name
        self.categories = [""]
        self.keywords = [""]
        self.colors = [""]
        self.sizes = [""]
        self.link = None
        self.any_color = False
        self.any_size = True

    def __repr__(self):
        return "{}".format(self.name)

class BillingInfo(object):

    def __init__(self, name, email, phone_num, address, city, zipcode):
        self.name = name
        self.email = email
        self.phone = phone_num
        self.address = address
        self.city = city
        self.zipcode = zipcode

    # def __repr__(self):
    #     return "Billing Info for {} is "

class CardInfo(object):

    def __init__(self, ctype, number, exp_month, exp_yr, cvv):
        self.ctype = ctype
        self.number = number
        self.exp_month = exp_month
        self.exp_yr = exp_yr
        self.cvv = cvv


class Buyer(object):

    def __init__(self, name, billing_info, card_info):
        self.name = name
        self.billing = billing_info
        self.card = card_info
        self.first_choice = None
        self.second_choice = None
        self.third_choice = None

# p = Product("jacket1", ["jackets"], ["Camo"], ["Red"], ["L"])
# home = BillingInfo("Ratuja Reddy", "ratuja@gmail.com", "630-779-9112", "5486 S Ellis Ave", "Chicago", "60615")
# debit = CardInfo("Mastercard", "5555222255559999", "03", "2020", "100")
# ratuja = Buyer("Ratuja", home, debit)