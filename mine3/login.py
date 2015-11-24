#_*_ coding: UTF-8 _*_
__author__ = 'evan'
import requests

import nomore_xueqiu
import nomore_mine
import logger


LOG = logger.get_loger()
LOGIN_XUEQIU = ''
LOGIN_MINE = ''

def _login(url, body, headers):
    session = requests.session()
    try:
        login_res = session.post(url, headers=headers, data=body)
    except Exception as e:
        LOG.error('login Fail: %s %s' % (url, e))
        return False
    else:
        LOG.warn('login : %d FOR %s' % (login_res.status_code, url))
        return session


def get_xueqiu_session():

    url = nomore_xueqiu.LOGIN_URL
    body = nomore_xueqiu.LOGIN_BODY
    headers = nomore_xueqiu.HEADERS
    return _login(url, body, headers)



def get_mine_session():
    global LOGIN_MINE
    if not LOGIN_MINE:
        url = 'https://stock.pingan.com.cn/pa/newstock/webTrade/cgi-bin/trade/Login?null'
        body = nomore_mine.LOGIN_BODY
        session = requests.session()
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/'
                                 '537.36 (KHTML, like Gecko) Chrome/46.0.2490.80'
                                 ' Safari/537.36',
                   'Host':'stock.pingan.com.cn',
                   'Origin':'https://stock.pingan.com.cn',
                   'Referer':'https://stock.pingan.com.cn/pa/newstock/webTrade/'
                             'cgi-bin/trade/Login?logout=true',
                   'Upgrade-Insecure-Requests': '1',
                   'Content-Type':'application/x-www-form-urlencoded',
                   'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                   'Accept-Encoding':'gzip, deflate',
                   'Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
                   'Cache-Control':'max-age=0',
                   'Connection':'keep-alive',
                   }
        cookie = nomore_mine.COOKIES

        try:
            for k, v in cookie.items():
                session.cookies.set(name=k, value=v)
            login_res = session.post(url, headers=headers, data=body, verify = False)
        except Exception as e:
            LOG.error('login Fail: %s %s' % (url, e))
            return False
        else:
            LOG.warn('login : %d FOR %s' % (login_res.status_code, url))
            LOGIN_MINE = session
    return LOGIN_MINE
