#_*_ coding: UTF-8 _*_
__author__ = 'evan'

import time

from const import HEADERS_MINE
import logger
import login
import nomore_mine

LOG = logger.get_loger()


def buy(session, code, price):
    quant = price
    url = nomore_mine.TRANSACT_URL
    body = nomore_mine.BUY_BODY
    body['SECU_CODE'] = code
    res = session.post(url, headers=HEADERS_MINE,
                             data=body)
    LOG.warn('market buy: %d %s' % (res.status_code, res.content))

def get_history(session):
    url = nomore_mine.TRANSACT_URL
    body = nomore_mine.HISTORY_BODY
    try:
        res = session.post(url, headers=HEADERS_MINE, data=body)
    except Exception as e:
        LOG.error('history Fail :%s' % e)
    else:
        LOG.warn('history: %d %s' % (res.status_code, res.content))

def get_balance(session):
    url = nomore_mine.TRANSACT_URL
    body = nomore_mine.BALANCE_BODY
    try:
        res = session.post(url, headers=HEADERS_MINE, data=body)
        content = res.content.decode('iconv','ignore')
        print('XVLC' in content)
    except Exception as e:
        LOG.error('get balance Fail :%s' % e)
        return False
    else:

        balance = float(content)
        LOG.warn('get balance: %d %f' % (res.status_code, balance))
        print(balance)
        return balance

def keep_awake(session):
    url = nomore_mine.TRANSACT_URL
    body = nomore_mine.LOCK_BODY
    res = session.post(url, headers=HEADERS_MINE, data=body)
    LOG.warn('keep awake: %d %s' % (res.status_code, res.content))


if __name__ == '__main__':
    session = login.get_mine_session()
    while True:
        keep_awake(session)
        get_history(session)
        get_balance(session)
        time.sleep(600)


