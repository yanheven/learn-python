#_*_ coding: UTF-8 _*_
#__author__ = 'evan'
import logger
import login
import nomore_mine

LOG = logger.get_loger()


def buy(session, code, price):
    # balance = 23900
    # if not balance:
    #     return False
    # quantity = int(balance / price / 100) * 100
    quantity = 1200
    url = nomore_mine.TRANSACT_URL
    body = nomore_mine.BUY_BODY
    body['SECU_CODE'] = code
    body['QTY'] = quantity
    body['PRICE'] = 17.2
    try:
        res = session.post(url, headers=nomore_mine.HEADERS,
                           data=body)
    except Exception as e:
        LOG.error('market buy Fail %s' % e)
    else:
        LOG.warn('market buy: %d %s code: %s quantity: %d' %
                 (res.status_code, res.content, code, quantity))


def get_history(session):
    url = nomore_mine.TRANSACT_URL
    body = nomore_mine.HISTORY_BODY
    try:
        res = session.post(url, headers=nomore_mine.HEADERS, data=body)
    except Exception as e:
        LOG.error('history Fail :%s' % e)
    else:
        LOG.warn('history: %d %s' % (res.status_code, res.content))

def get_balance(session):
    url = nomore_mine.TRANSACT_URL
    body = nomore_mine.BALANCE_BODY
    try:
        res = session.post(url, headers=nomore_mine.HEADERS, data=body)
        content = res.content

    except Exception as e:
        LOG.error('get balance Fail :%s' % e)
        return False
    else:

        balance = float(content)
        LOG.warn('get balance: %d balance: %f' % (res.status_code, balance))
        return balance


def keep_awake(session):
    url = nomore_mine.TRANSACT_URL
    body = nomore_mine.LOCK_BODY
    try:
        res = session.post(url, headers=nomore_mine.HEADERS, data=body)
    except Exception as e:
        LOG.error('keep awake Fail :%s' % e)
        return False
    else:
        LOG.warn('keep awake: %d' % (res.status_code))


if __name__ == '__main__':
    session = login.get_mine_session()
    keep_awake(session)
    import time
    while True:
        get_history(session)
        time.sleep(1800)

