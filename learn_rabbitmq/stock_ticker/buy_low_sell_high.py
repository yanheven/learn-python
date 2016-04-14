import pickle
import random
import uuid

class Buyer(object):
    def __init__(self, client, qname, trend=5):
        self.holdings = {}
        self.cash = 100000.0
        self.history = {}
        self.qname = qname
        self.client = client
        self.trend = trend
        self.qname = uuid.uuid4().hex

    def decide_whether_to_buy_or_sell(self, quote):
        symbol, price, date, counter = quote
        #print "Thinking about whether to buy or sell %s at %s" % (symbol, price)

        if symbol not in self.history:
            self.history[symbol] = [price]
        else:
            self.history[symbol].append(price)

        if len(self.history[symbol]) >= self.trend:
            price_low = min(self.history[symbol][-self.trend:])
            price_max = max(self.history[symbol][-self.trend:])
            price_avg = sum(self.history[symbol][-self.trend:])/self.trend
            print "Recent history of %s is %s" % (symbol, self.history[symbol][-self.trend:])
        else:
            price_low, price_max, price_avg = (-1, -1, -1)
            print "%s quotes until we start deciding whether to buy or sell %s" % (self.trend - len(self.history[symbol]), symbol)
            #print "Recent history of %s is %s" % (symbol, self.history[symbol])

        if price_low == -1: return

        #print "Trending minimum/avg/max of %s is %s-%s-%s" % (symbol, price_low, price_avg, price_max)
        #for symbol in self.holdings.keys():
        #    print "self.history[symbol][-1] = %s" % self.history[symbol][-1]
        #    print "self.holdings[symbol][0] = %s" % self.holdings[symbol][0]
        #    print "Value of %s is %s" % (symbol, float(self.holdings[symbol][0])*self.history[symbol][-1])
        value = sum([self.holdings[symbol][0]*self.history[symbol][-1] for symbol in self.holdings.keys()])
        print "Net worth is %s + %s = %s" % (self.cash, value, self.cash + value)

        if symbol not in self.holdings:
            if price < 1.01*price_low:
                shares_to_buy = random.choice([10, 15, 20, 25, 30])
                print "I don't own any %s yet, and the price is below the trending minimum of %s so I'm buying %s shares." % (symbol, price_low, shares_to_buy)
                cost = shares_to_buy * price
                print "Cost is %s, cash is %s" % (cost, self.cash)
                if cost < self.cash:
                    self.holdings[symbol] = (shares_to_buy, price, cost)
                    self.cash -= cost
                    print "Cash is now %s" % self.cash
                else:
                    print "Unfortunately, I don't have enough cash at this time."
        else:
            if price > self.holdings[symbol][1] and price > 0.99*price_max:
                print "+++++++ Price of %s is higher than my holdings, so I'm going to sell!" % symbol
                sale_value = self.holdings[symbol][0] * price
                print "Sale value is %s" % sale_value
                print "Holdings value is %s" % self.holdings[symbol][2]
                print "Total net is %s" % (sale_value - self.holdings[symbol][2])
                self.cash += sale_value
                print "Cash is now %s" % self.cash
                del self.holdings[symbol]

    def handle_pyamqplib_delivery(self, channel, method, properties,
                                                 body):
        self.handle(channel, 0, body)

    def handle(self, ch, delivery_tag, body):
        quote = pickle.loads(body)
        #print "New price for %s => %s at %s" % quote
        ch.basic_ack(delivery_tag = delivery_tag)
        print "Received message %s" % quote[3]
        self.decide_whether_to_buy_or_sell(quote)

    def monitor(self):
        self.client.monitor(self.qname, self.handle_pyamqplib_delivery)
