import csv

def read_csv(file_name):
    reader = csv.reader(open(file_name))
    reader = list(reader)[1:]
    ret = []
    for i in reader:
        detail = i[0].split('\t')
        ret.append(detail)
    return ret

def get_buyer(file_name):
    buyers = read_csv(file_name)
    buyer_dicts = []
    for i in buyers:
        buyer_dict = {}
        buyer_dict['order_id'] = i[0]
        buyer_dict['buyer_email'] = i[10]
        buyer_dict['buyer_name'] = i[11].split(' ')[0]
        buyer_dict['sku'] = i[13]
        buyer_dicts.append(buyer_dict)
    return buyer_dicts

def get_product_name(file_name):
    """{'sku':{'asin': 'xxxx', 'product_name': 'ssss'}}

    :param file_name:
    :return:
    """
    products = read_csv(file_name)
    product_dicts = {}
    for i in products:
        product_dict = {}
        product_dict['asin'] = i[2]
        product_dict['product_name'] = i[3]
        product_dict['market_domain'] = i[1]
        product_dicts[i[0]] = product_dict
    return product_dicts

def get_refund(file_name):
    refunds = read_csv(file_name)
    refund_ids = []
    for i in refunds:
        refund_ids.append(i[1])
    return refund_ids

if __name__ == '__main__':
    ret_list = read_csv('399905.csv')
    ret_list = read_csv('399905.csv')
    print(ret_list[-1])
