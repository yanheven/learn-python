import pika


def on_channel_open(channel):
    channel.basic_publish()

def on_open(conn):
    conn.channel(on_channel_open)


class PikaPublisher(object):
    def __init__(self, exchange_name):
        self.exchange_name = exchange_name
        self.queue_exists = False
        self.conn = None
        self.stop = False

    def publish(self, message, routing_key):
        conn = pika.BlockingConnection(pika.ConnectionParameters(
                '127.0.0.1',
                credentials=pika.PlainCredentials('guest', 'guest')))

        ch = conn.channel()

        ch.exchange_declare(exchange=self.exchange_name, type="fanout", durable=False, auto_delete=False)

        ch.basic_publish(exchange=self.exchange_name,
                         routing_key=routing_key,
                         body=message,
                         properties=pika.BasicProperties(
                                content_type = "text/plain",
                                delivery_mode = 2, # persistent
                                ))
        ch.close()
        conn.close()

    def on_connected(self, unused_conn):
        """Called when we are fully connected to RabbitMQ"""
        # Open a channel
        self.add_on_connection_close_callback()
        self.open_channel()

    def open_channel(self):
        """Open a new channel with RabbitMQ by issuing the Channel.Open RPC
        command. When RabbitMQ responds that the channel is open, the
        on_channel_open callback will be invoked by pika.

        """
        print('Creating a new channel')
        self.conn.channel(on_open_callback=self.on_channel_open)

    # Step #3
    def on_channel_open(self, new_channel):
        """Called when our channel has opened"""
        print('open channel')
        self.channel = new_channel
        self.add_on_channel_close_callback()
        self.channel.queue_declare(queue=self.qname, durable=True, exclusive=False, auto_delete=False,
                                   callback=self.on_queue_declared)

    def add_on_channel_close_callback(self):
        """This method tells pika to call the on_channel_closed method if
        RabbitMQ unexpectedly closes the channel.

        """
        print('Adding channel close callback')
        self.channel.add_on_close_callback(self.on_channel_closed)

    def on_channel_closed(self, channel, reply_code, reply_text):
        """Invoked by pika when RabbitMQ unexpectedly closes the channel.
        Channels are usually closed if you attempt to do something that
        violates the protocol, such as re-declare an exchange or queue with
        different parameters. In this case, we'll close the connection
        to shutdown the object.

        :param pika.channel.Channel: The closed channel
        :param int reply_code: The numeric reason the channel was closed
        :param str reply_text: The text reason the channel was closed

        """
        print('Channel %i was closed: (%s) %s', channel, reply_code, reply_text)
        self.conn.close()

    # Step #4
    def on_queue_declared(self, frame):
        """Called when RabbitMQ has told us our Queue has been declared, frame is the response from RabbitMQ"""
        self.channel.queue_bind(queue=self.qname, exchange=self.exchange_name, routing_key=self.qname,
                           callback=self.on_queue_bind)
        print "Binding queue %s to exchange %s" % (self.qname, self.exchange_name)

    def on_queue_bind(self, frame):
        self.channel.basic_consume(self.callback, queue=self.qname)

    def reconnect(self):
        self.conn.ioloop.stop()
        if not self.stop:
            self.conn = self.connect()
            self.conn.ioloop.start()

    def add_on_connection_close_callback(self):
        """This method adds an on close callback that will be invoked by pika
        when RabbitMQ closes the connection to the publisher unexpectedly.

        """
        print('Adding connection close callback')
        self.conn.add_on_close_callback(self.on_connection_closed)

    def on_connection_closed(self, reply_code, reply_text):
        if self.stop:
            self.conn.ioloop.stop()
        else:
            print('Connection closed, reopening in 5 seconds: (%s) %s',
                           reply_code, reply_text)
            self.conn.add_timeout(2, self.reconnect())

    # # Step #5
    # def handle_delivery(channel, method, header, body):
    #     """Called when we receive a message from RabbitMQ"""
    #     print body

    # Step #1: Connect to RabbitMQ using the default parameters
    def connect(self):
        conn = pika.SelectConnection(pika.ConnectionParameters(
            '127.0.0.1',
            credentials=pika.PlainCredentials('guest', 'guest')),
            self.on_connected,
            stop_ioloop_on_close=False)
        return conn

    def monitor(self, qname, callback):
        self.qname = qname
        self.callback = callback

        try:
            # Loop so we can communicate with RabbitMQ
            self.conn = self.connect()
            self.conn.ioloop.start()
        except KeyboardInterrupt:
            # Gracefully close the connection
            self.conn.close()
            # Loop until we're fully closed, will stop on its own
            self.conn.ioloop.start()

