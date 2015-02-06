__author__ = 'heven'
#!/usr/bin/env python
import pika
import time
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

for i in range(10000):
    msg=str(time.time())
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=msg)
    print msg
    time.sleep(0.001)
connection.close()