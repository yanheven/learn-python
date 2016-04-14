from pika_client import *
publisher = PikaPublisher(exchange_name="my_exchange")

########################################
# This part doesn't have to change
########################################

from ticker_system import *
ticker = Ticker(publisher, "")
ticker.monitor()
