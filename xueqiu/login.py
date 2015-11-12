#_*_ coding: UTF-8 _*_
__author__ = 'evan'
import requests

from const import HEADERS
import nomore_xueqiu
import nomore_mine
import logger


LOG = logger.get_loger()


def _login(url, body, header):
    session = requests.session()
    try:
        login_res = session.post(url, headers=header, data=body)
    except Exception as e:
        LOG.error('login Fail: %s %s' % (url ,e) )
        return False
    else:
        LOG.warn('login : %d FOR %s' % (login_res.status_code, url))
        return session


def get_xueqiu_session():

    url = nomore_xueqiu.LOGIN_URL
    body = nomore_xueqiu.LOGIN_BODY
    headers = HEADERS
    return _login(url, body, headers)


def get_mine_session():
    headers = HEADERS
    url = nomore_mine.LOGIN_URL
    body = nomore_mine.LOGIN_BODY
    session = _login(url, body, headers)
    url = nomore_mine.TRANSACT_URL
    body2 = nomore_mine.LOGIN_2
    body3 = nomore_mine.LOGIN_3
    try:
        login_res = session.post(url, headers=headers, data=body2)
        LOG.warn('login 2 : %d FOR %s' % (login_res.status_code, url))
        login_res = session.post(url, headers=headers, data=body3)
        LOG.warn('login 3 : %d FOR %s' % (login_res.status_code, url))
    except Exception as e:
        LOG.error('login Fail: %s  %s' % (url, e))
        return False
    else:
        return session
