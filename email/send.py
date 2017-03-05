# -*- coding: utf-8 -*-

# from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
import datetime
import csv


def read_csv(file_name):
    reader = csv.reader(open(file_name), delimiter='\t')
    return list(reader)[1:]


def get_buyer(file_name):
    buyers = read_csv(file_name)
    buyer_dicts = []
    yesterday = datetime.datetime.now() - datetime.timedelta(1)
    yesterday = yesterday.strftime('%Y-%m-%d')
    for i in buyers:
        if yesterday == i[44][:10]:
            buyer_dict = {}
            buyer_dict['order_id'] = i[0]
            buyer_dict['buyer_email'] = i[10]
            buyer_dict['buyer_name'] = i[11].split(' ')[0]
            buyer_dict['buyer_name'] = buyer_dict['buyer_name'].capitalize()
            buyer_dict['sku'] = i[13]
            buyer_dict['country'] = i[31]
            buyer_dicts.append(buyer_dict)
    return buyer_dicts


def get_product_name(file_name):
    """{'sku':{'asin': 'xxxx', 'product_name': 'ssss'}}

    :param file_name:
    :return:
    """
    products = read_csv(file_name)
    product_dicts = dict(com=dict(), ca=dict())
    for i in products:
        product_dict = {}
        product_dict['asin'] = i[2]
        product_dict['product_name'] = i[3]
        # product_dict['market_domain'] = i[1]
        product_dicts[i[1]][i[0]] = product_dict
    return product_dicts


def get_refund(file_name):
    refunds = read_csv(file_name)
    refund_ids = []
    for i in refunds:
        refund_ids.append(i[1])
    return refund_ids


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((
        Header(name, 'utf-8').encode(),
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))


# receivers = read_csv(raw_input('template name:'))
order_file_name = 'order.txt'
sku_file_name = 'sku.csv'
# refund_file_name = 'refund.txt'
buys = get_buyer(order_file_name)
skus = get_product_name(sku_file_name)
# refunds = get_refund(refund_file_name)
print(buys[0])

from_addr = 'amazon@ohilltech.com'
password = ''
to_addr = 'yanheven@qq.com'
smtp_server = 'smtp.exmail.qq.com'
alarm_str = '\nWarm Tips: After you choose your favorite nature sound,' \
            ' please remember to press the second button(♫ icon) on the' \
            ' backing again to save the setting.\n\nUser Manual: You can download the user' \
            ' manual on product page, go to "Product Information > Technical' \
            ' Specification > User Manual [pdf ]", or via this link https://images-na.ssl-' \
            'images-amazon.com/images/I/B18uhatYo2S.pdf\n'
follow_str = '''
Dear %s,

Greetings! This is Elena from O'Hill customer service team.

Please kindly be advised that we noticed that the package have delivered at you. May I know have you received it?

This is a follow-up email to confirm whether you are completely happy with this purchase.
If there was a problem with our product, please feel free to get back to us and we will help to get the problem solved ASAP.
And if you are satisfied with our product and service, we would greatly appreciate it if you could share your user experience
with your friends/ family or online.

The following is the details for your Amazon order: %s

%s
%s
To share your user experience, click: http://www.amazon.%s/dp/%s

If you have any problems about our product, we would appreciate it if you would give us a chance to make things right for you. Thanks a lot.

Wish you a great day ahead!

Best Regards,
Elena'''

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
send_account = 0
for i in buys:
    # if i['order_id'] in refunds:
    #     continue
    if 'US' == i['country']:
        sku_info = skus['com'].get(i['sku'])
        market_domain = 'com'
    elif 'CA' == i['country']:
        sku_info = skus['ca'].get(i['sku'])
        market_domain = 'ca'
    if not sku_info:
        miss_sku.append(i['sku'])
        continue
    extra_str = ''
    asin = sku_info['asin']
    if 'B01N9AMYWA' == asin:
        extra_str = alarm_str
    product_name = sku_info['product_name']
    msg = MIMEText(follow_str % (i['buyer_name'], i['order_id'], product_name,
                                 extra_str, market_domain, asin),
                   'plain', 'utf-8')
    msg['From'] = 'O\'Hill Direct<%s>' % from_addr
    msg['To'] = '%s<%s>' % (i['buyer_name'], i['buyer_email'])
    msg['Subject'] = Header('This is a follow-up letter about your Amazon'
                            ' Order #%s' % i['order_id'])

    print('sending to ...%s' % i['buyer_email'])
    server.sendmail(from_addr, [i['buyer_email']], msg.as_string())
    # server.sendmail(from_addr, to_addr, msg.as_string())
    print('sent to %s' % i['buyer_email'])
    send_account += 1

total_buyers = len(buys)
print('total buyers:%d, sent emails: %d' % (total_buyers, send_account))

if miss_sku:
    print('Miss sku:')
    for i in miss_sku:
        print(i)
server.quit()
