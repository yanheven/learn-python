#_*_ coding: UTF-8 _*_
__author__ = 'evan'

from const import HEADERS_MINE
import logger
import login
import nomore_mine


LOG = logger.get_loger()


def transact():

    url = nomore_mine.TRANSACT_URL
    # HEADERS['Referer'] = 'http://xueqiu.com/p/update?action=holdings&symbol=ZH672409'
    session = login.get_mine_session()
    body = nomore_mine.BUY_BODY
    res = session.post(url, headers=HEADERS_MINE,
                             data=body)
    LOG.warn('market buy: %d %s' % (res.status_code, res.content))

def get_history():
    url = nomore_mine.TRANSACT_URL
    session = login.get_mine_session()
    body = nomore_mine.HISTORY_BODY
    res = session.post(url, headers=HEADERS_MINE, data=body)
    LOG.warn('history: %d %s' % (res.status_code, res.content))


if __name__ == '__main__':
    get_history()
    # transact()