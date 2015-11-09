#_*_ coding: UTF-8 _*_
__author__ = 'evan'
import json
import random
import requests
import time

from const import headers
import login


origin_hold = ''

def rebalance(body):
    rebalance_url = 'http://xueqiu.com/cubes/rebalancing/create.json'
    session = login.get_session()
    headers['Referer'] = 'http://xueqiu.com/p/update?action=holdings&symbol=ZH672409'
    rebalance_res = session.post(rebalance_url, headers=headers,
                             data=body)
    print('rebalance', rebalance_res)


def get_hold(url):
    res = requests.get(url, headers=headers)
    print('get change', res)
    holdings = res.content
    holdings = holdings.split('SNB.cubeInfo = ')[1].split('SNB.cubePieData')[0]
    holdings = json.loads(holdings,encoding='utf-8').get('view_rebalancing').get('holdings')
    hold = {}
    holdings_str = '''['''
    cash = 100
    # sorted(holdings, key=lambda x: x['stock_id'])
    for i in holdings:
        for k, v in i.items():
            if k == 'weight':
                cash -= v
            if type(v) == unicode:
                hold[k] = v.encode('utf-8')
            else:
                hold[k] = v
        if hold['weight'] > 0:
            stock_id = hold['stock_id']
            weight = hold['weight']
            segment_name = hold['segment_name']
            holdings_str += '''{"stock_id":%s,"weight":%s,"segment_name":"%s"},'''%\
                       (stock_id, weight, segment_name)
    holdings_str = holdings_str[:-1] + ''']'''
    hold_body = {'cash':str(cash),'holdings':holdings_str}
    return hold_body, cash


def follow():
    other_url = 'http://xueqiu.com/P/ZH010389'
    other_hold, cash = get_hold(other_url)
    global origin_hold
    if not origin_hold:
        origin_hold = json.dumps(other_hold)
    elif origin_hold != json.dumps(other_hold):
        other_hold['cube_symbol'] = 'ZH672409'
        other_hold['segment'] = 'true'
        other_hold['comment'] = '老刀:I am back.'
        rebalance(other_hold)
        return cash < 1
    return False


if __name__ == '__main__':
    while True:
        if follow():
            break
        time.sleep(random.randint(1,5))
