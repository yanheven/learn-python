#_*_ coding: UTF-8 _*_
__author__ = 'evan'
import requests

from const import HEADERS
import nomore_xueqiu
import nomore_mine
import logger


LOG = logger.get_loger()


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
    headers = HEADERS
    return _login(url, body, headers)


def get_mine_session():
    # headers = HEADERS
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
               'Cookie': 'BIGipServersis-pa18-trade_30548=!xqfSETm0oKx7o1kgDmryxEeVcET6n52rQKd8D88qPK6NyLpLqP9UsCqxxAMTKmwu2ENi27G6wPkABQ==; BIGipServersis-pa18-hq_30548=!ua5OSRf5aR7AMpkgDmryxEeVcET6n2oOY3mmpTkO2k5m5Zsp7L9C/DDcg5/6sEiD5GANB2ML1J7mFg==; tradePa18SessionId=HLx1WGTd2WqCThlTc0jVFXh90TxFDMn1T4x9hBGq1gf3z2hrbnt1!1297596384; WT-FPC=id=211.161.198.135-3704427840.30454585:lv=1447333633797:ss=1447333633797:fs=1447333633797:pn=1:vn=1'
               }
    cookie = {'BIGipServersis-pa18-trade_30548':'!xqfSETm0oKx7o1kgDmryxEeVcET6n52rQKd8D88qPK6NyLpLqP9UsCqxxAMTKmwu2ENi27G6wPkABQ==',
              'BIGipServersis-pa18-hq_30548':'!ua5OSRf5aR7AMpkgDmryxEeVcET6n2oOY3mmpTkO2k5m5Zsp7L9C/DDcg5/6sEiD5GANB2ML1J7mFg==',
              'tradePa18SessionId':'HLx1WGTd2WqCThlTc0jVFXh90TxFDMn1T4x9hBGq1gf3z2hrbnt1!1297596384',
              'WT-FPC':'id=211.161.198.135-3704427840.30454585:lv=1447333633797:ss=1447333633797:fs=1447333633797:pn=1:vn=1',
              }

    try:
        for k, v in cookie.items():
            session.cookies.set(name=k, value=v)
        login_res = session.post(url, headers=headers, data=body)
    except Exception as e:
        LOG.error('login Fail: %s %s' % (url, e))
        return False
    else:
        LOG.warn('login : %d FOR %s' % (login_res.status_code, url))

        return session
