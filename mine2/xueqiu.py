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
import mine

origin_hold_000979 = ''
origin_hold_010389 = ''
origin_hold_016097 = ''

LOG = logger.get_loger()


def rebalance(body):
    rebalance_url = 'http://xueqiu.com/cubes/rebalancing/create.json'
    session = login.get_session()
    if not session:
        return
    HEADERS['Referer'] = 'http://xueqiu.com/p/update?action=holdings&symbol=ZH672409'
    try:
        rebalance_res = session.post(rebalance_url, headers=HEADERS,
                             data=body)
    except Exception as e:
        LOG.warn('rebalance Fail: %s '%e)
        return
    del HEADERS['Referer']
    LOG.warn('rebalance: %d %s' % (rebalance_res.status_code, body['cube_symbol']))


def get_hold(url):
    res = requests.get(url, headers=HEADERS)
    LOG.warn('get change: %d %s' % (res.status_code, url))
    holdings = res.content
    holdings = holdings.split('SNB.cubeInfo = ')[1].split('SNB.cubePieData')[0]
    content = json.loads(holdings,encoding='utf-8')
    holdings = content.get('view_rebalancing').get('holdings')
    history_holdings = content.get('sell_rebalancing').get('rebalancing_histories')
    holdings_str = '''['''
    cash = 100
    code = holdings[-1]['stock_symbol'][2:]
    for i in holdings:
        weight = i['weight']
        cash -= weight
        if weight > 0:
            stock_id = i['stock_id']
            for his in history_holdings:
                if his['stock_id'] == stock_id:
                    price = his['price']
            segment_name = i['segment_name'].encode('utf-8')
            holdings_str += '''{"stock_id":%s,"weight":%s,"segment_name":"%s"},'''%\
                       (stock_id, weight, segment_name)
    holdings_str = holdings_str[:-1] + ''']'''
    hold_body = {'cash':str(cash),'holdings':holdings_str}
    LOG.warn('get change: code : %s price: %f' % (code, price))
    return hold_body, cash, code, price


def follow_010389():
    other_url = 'http://xueqiu.com/P/ZH010389'
    try:
        other_hold, cash, code, price = get_hold(other_url)
    except Exception as e:
        LOG.error('get change ERROR: %s' % e)
    else:
        global origin_hold_010389
        if not origin_hold_010389:
            origin_hold_010389 = json.dumps(other_hold)
        elif origin_hold_010389 != json.dumps(other_hold):
            session = login.get_mine_session()
            mine.buy(session, code, price)
            other_hold['cube_symbol'] = 'ZH672409'
            other_hold['segment'] = 'true'
            other_hold['comment'] = '老刀:I am back.'
            rebalance(other_hold)
            return cash < 1
    return False


# def follow_000979():
#     other_url = 'http://xueqiu.com/P/ZH000979'
#     try:
#         other_hold, cash, price= get_hold(other_url)
#     except Exception as e:
#         print(e)
#     else:
#         global origin_hold_000979
#         hold_json =json.dumps(other_hold)
#         if not origin_hold_000979:
#             origin_hold_000979 = hold_json
#         elif origin_hold_000979 != hold_json:
#             for i in xrange(len(hold_json)):
#                 if hold_json[i] != origin_hold_000979[i]:
#                     print(origin_hold_000979[:i+1])
#                     print(hold_json[:i+1])
#                     break
#             other_hold['cube_symbol'] = 'ZH675871'
#             other_hold['segment'] = 'true'
#             other_hold['comment'] = '老刀:I am back.'
#             rebalance(other_hold)
#             return cash < 1
#     return False


# def follow_016097():
#     other_url = 'http://xueqiu.com/P/ZH016097'
#     try:
#         other_hold, cash = get_hold(other_url)
#     except Exception as e:
#         print(e)
#     else:
#         global origin_hold_016097
#         hold_json =json.dumps(other_hold)
#         if not origin_hold_016097:
#             origin_hold_016097 = hold_json
#         elif origin_hold_016097 != hold_json:
#             other_hold['cube_symbol'] = 'ZH675871'
#             other_hold['segment'] = 'true'
#             other_hold['comment'] = '老刀:I am back.'
#             rebalance(other_hold)
#             return cash < 1
#     return False


if __name__ == '__main__':
    flag_done_010389 = True
    while True:

        if flag_done_010389:
            time.sleep(1)
            if follow_010389():
                flag_done_010389 = False
        if not flag_done_010389:
            break
        hour = time.strftime('%H')
        minitu = int(time.strftime('%S'))
        if minitu % 10 == 1:
            session = login.get_mine_session()
            mine.keep_awake(session)
            mine.get_history(session)
        if hour == '7':
            break
