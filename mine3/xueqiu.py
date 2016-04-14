#_*_ coding: UTF-8 _*_
__author__ = 'evan'
import json
import requests
import time
import sys

import logger
import login
import mine
import nomore_xueqiu

origin_hold_000979 = None
origin_hold_010389 = None
origin_hold_016097 = None

LOG = logger.get_loger()
reload(sys)
sys.setdefaultencoding('utf-8')


def get_price(code):
    url = 'http://hq.sinajs.cn/list=' + code
    res = requests.get(url)
    price = float(res.content.split(',')[3])
    return price


def rebalance(body):
    rebalance_url = 'http://xueqiu.com/cubes/rebalancing/create.json'
    session = login.get_xueqiu_session()
    if not session:
        return
    headers = nomore_xueqiu.HEADERS
    headers['Referer'] = 'http://xueqiu.com/p/update?action=holdings&symbol=ZH672409'
    try:
        rebalance_res = session.post(rebalance_url, headers=headers,
                             data=body)
    except Exception as e:
        LOG.warn('rebalance Fail: %s '%e)
        return
    else:
        LOG.warn('rebalance: %d %s' % (rebalance_res.status_code, body['cube_symbol']))
    finally:
        del headers['Referer']


def get_hold(url):
    res = requests.get(url, headers=nomore_xueqiu.HEADERS)
    holdings = res.content
    holdings = holdings.split('SNB.cubeInfo = ')[1].split('SNB.cubePieData')[0]
    content = json.loads(holdings,encoding='utf-8')
    holdings = content.get('view_rebalancing').get('holdings')
    # history_holdings = content.get('sell_rebalancing').get('rebalancing_histories')
    holdings_str = '''['''
    cash = 100
    code = '0'
    price = 0
    for i in holdings:
        weight = i['weight']
        cash -= weight
        if weight > 90:
            code = i['stock_symbol'][2:]
            stock_id = i['stock_id']
           #  for his in history_holdings:
           #    if his['stock_id'] == stock_id:
           #          price = his['price']
            sinacode = i['stock_symbol'][:2].lower() + code
            price = get_price(sinacode)
            segment_name = i['segment_name'].encode('utf-8')
            holdings_str += '''{"stock_id":%s,"weight":%s,"segment_name":"%s"},'''%\
                       (stock_id, weight, segment_name)
    holdings_str = holdings_str[:-1] + ''']'''
    hold_body = {'cash': str(cash), 'holdings': holdings_str}
    if price:
        return hold_body, cash, code, price
    return 0, 0, '0', 0


def follow_010389(mine_session):
    other_url = 'http://xueqiu.com/P/ZH010389'
    try:
        other_hold, cash, code, price = get_hold(other_url)
    except Exception as e:
        LOG.error('get change ERROR: %s' % e)
    else:
        global origin_hold_010389
        if origin_hold_010389 is None:
            origin_hold_010389 = code
        elif origin_hold_010389 != code:
            mine.buy(mine_session, code, price)
            other_hold['cube_symbol'] = 'ZH672409'
            other_hold['segment'] = 'true'
            other_hold['comment'] = ''
            if not code.startswith('3'):
                rebalance(other_hold)
            return cash < 1
        LOG.warn('get change: code : %s price: %f' % (code, price))
    return False


if __name__ == '__main__':
    flag_done_010389 = True
    mine_session = login.get_mine_session()
    mine.get_history(mine_session)
    while True:
        if flag_done_010389:
            if follow_010389(mine_session):
                flag_done_010389 = False
        if not flag_done_010389:
            break
        hour = time.strftime('%H')
        if hour == '15':
            break
