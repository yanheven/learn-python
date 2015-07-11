__author__ = 'heven'
#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

print ' [*] Waiting for messages. To exit press CTRL+C'
timestart=0

def callback(ch, method, properties, body):
    timenow=float(body)
    if timestart==0:
        timestamp=timenow

    elif timenow<timestart:
        print "error"
    print body

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

channel.start_consuming()
