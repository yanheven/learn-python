from pika_client import *
publisher = PikaPublisher(exchange_name="my_exchange")

########################################
# This part doesn't have to change
########################################

from buy_low_sell_high import *
buyer = Buyer(publisher, "", trend=25)
print "Buyer = %s" % id(buyer)
buyer.monitor()
