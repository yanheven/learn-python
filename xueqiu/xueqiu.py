#_*_ coding: UTF-8 _*_
__author__ = 'evan'
import json
import random
import requests
import time

from const import HEADERS
import emailer
import logger
import login
from time_util import get_format_time


origin_hold_000979 = ''
origin_hold_010389 = ''
origin_hold_016097 = ''

LOG = logger.get_loger()


def rebalance(body):
    rebalance_url = 'http://xueqiu.com/cubes/rebalancing/create.json'
    session = login.get_session()
    HEADERS['Referer'] = 'http://xueqiu.com/p/update?action=holdings&symbol=ZH672409'
    rebalance_res = session.post(rebalance_url, headers=HEADERS,
                             data=body)
    del HEADERS['Referer']
    # print get_format_time(),
    # print('rebalance', rebalance_res)
    LOG.warn('rebalance: %d %s' % (rebalance_res.status_code, body['cube_symbol']))


def get_hold(url):
    res = requests.get(url, headers=HEADERS)
    # print get_format_time(),
    # print('get change', res),
    # print(url)
    LOG.warn('get change: %d %s' % (res.status_code, url))
    holdings = res.content
    holdings = holdings.split('SNB.cubeInfo = ')[1].split('SNB.cubePieData')[0]
    holdings = json.loads(holdings,encoding='utf-8').get('view_rebalancing').get('holdings')
    hold = {}
    holdings_str = '''['''
    cash = 100
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


def follow_010389():
    other_url = 'http://xueqiu.com/P/ZH010389'
    try:
        other_hold, cash = get_hold(other_url)
    except Exception as e:
        # print(e)
        LOG.error('get change ERROR: %s' % e)
    else:
        global origin_hold_010389
        if not origin_hold_010389:
            origin_hold_010389 = json.dumps(other_hold)
        elif origin_hold_010389 != json.dumps(other_hold):
            other_hold['cube_symbol'] = 'ZH672409'
            other_hold['segment'] = 'true'
            other_hold['comment'] = '老刀:I am back.'
            rebalance(other_hold)
            return cash < 1
    return False


def follow_000979():
    other_url = 'http://xueqiu.com/P/ZH000979'
    try:
        other_hold, cash = get_hold(other_url)
    except Exception as e:
        print(e)
    else:
        global origin_hold_000979
        hold_json =json.dumps(other_hold)
        if not origin_hold_000979:
            origin_hold_000979 = hold_json
        elif origin_hold_000979 != hold_json:
            for i in xrange(len(hold_json)):
                if hold_json[i] != origin_hold_000979[i]:
                    print(origin_hold_000979[:i+1])
                    print(hold_json[:i+1])
                    break
            other_hold['cube_symbol'] = 'ZH675871'
            other_hold['segment'] = 'true'
            other_hold['comment'] = '老刀:I am back.'
            rebalance(other_hold)
            return cash < 1
    return False


def follow_016097():
    other_url = 'http://xueqiu.com/P/ZH016097'
    try:
        other_hold, cash = get_hold(other_url)
    except Exception as e:
        print(e)
    else:
        global origin_hold_016097
        hold_json =json.dumps(other_hold)
        if not origin_hold_016097:
            origin_hold_016097 = hold_json
        elif origin_hold_016097 != hold_json:
            other_hold['cube_symbol'] = 'ZH675871'
            other_hold['segment'] = 'true'
            other_hold['comment'] = '老刀:I am back.'
            rebalance(other_hold)
            return cash < 1
    return False


if __name__ == '__main__':
    flag_016097 = True
    flag_010389 = True
    while True:
        if flag_016097:
            time.sleep(1)
            if follow_016097():
                flag_016097 = False
        if flag_010389:
            time.sleep(1)
            if follow_010389():
                flag_010389 = False
        if not (flag_010389 or flag_016097):
            break
        hour = time.strftime('%H')
        if hour == '7':
            break
