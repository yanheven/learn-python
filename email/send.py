# -*- coding: utf-8 -*-

# from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

from get_receivers import get_buyer
from get_receivers import get_product_name
from get_receivers import get_refund

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

# receivers = read_csv(raw_input('template name:'))
order_file_name = 'order.txt'
sku_file_name = 'sku.csv'
refund_file_name = 'refund.txt'
buys = get_buyer(order_file_name)
skus = get_product_name(sku_file_name)
refunds = get_refund(refund_file_name)
print(buys[0])

from_addr = 'amazon@ohilltech.com'
password = ''
to_addr = 'yanheven@qq.com'
smtp_server = 'smtp.exmail.qq.com'

smtp_port = 465
print('1...')
server = smtplib.SMTP_SSL(smtp_server, smtp_port)
print('starttls...')
# server.starttls()
# 剩下的代码和前面的一模一样:
server.set_debuglevel(1)
print('login...')
server.login(from_addr, password)
miss_sku = []
for i in buys:
    if i['order_id'] in refunds:
        continue
    sku_info = skus.get(i['sku'])
    if not sku_info:
        miss_sku.append(i['sku'])
        continue
    market_domain = sku_info['market_domain']
    asin = sku_info['asin']
    product_name = sku_info['product_name']
    msg = MIMEText('''
Dear %s,

Greetings! This is Elena from O'Hill customer service team.

This is a follow-up email to confirm whether you are completely happy with this purchase. If there was a problem with our product, please feel free to get back to us and we will help to get the problem solved ASAP. And if you are satisfied with our product and service, we would greatly appreciate it if you could share your user experience with your friends/ family or online.

The following is the details for your Amazon order: %s

%s

To share your user experience, click: http://www.amazon.%s/dp/%s

This email is for you to be completely satisfied with this transaction. If this is not the case, we would appreciate it if you would give us a chance to make things right for you before leaving a feedback. Thanks a lot.

Wish you a great day ahead!

Best Regards,
Elena''' % (i['buyer_name'], i['order_id'], product_name, market_domain, asin), 'plain', 'utf-8')
    msg['From'] = u'O\'Hill Direct<%s>' % from_addr
    msg['To'] = u'%s<%s>' % (i['buyer_name'], i['buyer_email'])
    msg['Subject'] = Header('This is a follow-up letter about your Amazon'
                            ' Order #%s' % i['order_id'])

    # server = smtplib.SMTP(smtp_server, 25)
    print('sending to ...%s' % i['buyer_email'])
    server.sendmail(from_addr, [i['buyer_email']], msg.as_string())
    print('sent to %s' % i['buyer_email'])

if miss_sku:
    print('Miss sku:')
    for i in miss_sku:
        print(i)
server.quit()

