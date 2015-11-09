__author__ = 'evan'
import requests

def http_get_json(url):
    res_body = {}
    try:
        res = requests.get(url)
        res_body = res.json()
    except Exception as e:
        print(e)
    return res_body

def get_users():
    url = 'http://c9t16285.itcs.hpecorp.net:7001/customer'
    res_body = http_get_json(url=url)
    users = res_body.get('customers')
    user_ids = [i['id'] for i in users]
    print('users amount%d'%len(user_ids))
    return user_ids

def get_user_offering(user_id):
    url = \
        'http://c9t16285.itcs.hpecorp.net:7001/catalog/offeringtype/customer/'
    url += str(user_id)
    res_body = http_get_json(url=url)
    offerings = res_body.get('offerings')
    offering_ids = [i['id'] for i in offerings]
    return offering_ids

def main():
    user_ids = get_users()
    # for i in xrange(417):
    #     if user_ids[i] == 100020:
    #         print user_ids[i+1]
    flag = False
    for id in user_ids:
        if id == 100214:
            flag = not flag
            continue
        if flag:
            offering_ids = get_user_offering(id)
            if 10 in offering_ids and 11 in offering_ids and 10008 in offering_ids:
                print(id)
            print('-',id ,offering_ids)
    print('done')

if __name__ == '__main__':
    main()
