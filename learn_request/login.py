# _*_ coding: UTf-8 _*_
__author__ = 'evan'
import requests
import datetime
import time
import json
import urllib

def get_login_session(url, data=None):
    session = requests.session()
    time_now = str(int(time.time() * 1000))
    if data is None:
        date = {'_':time_now}
    res = session.get(url,data)
    return session

def get_xueqiu_login_session():
    base_url = 'http://xueqiu.com'
    pre_url ='http://xueqiu.com/service/csrf?_='
    login_url = 'http://xueqiu.com/user/login'
    main_page_url = 'http://xueqiu.com/yanheven'
    rebance_url = 'http://xueqiu.com/cubes/rebalancing/create.json'
    update_url = 'http://xueqiu.com/cubes/update.json'

    data = {'username': 'yanheven@qq.com', 'areacode': '86', 'telephone': '',
            'remember_me': '1', 'password':'60DCCC0E54F96005ECAB40CA9762CB83'}
    time_now = str(int(time.time() * 1000))
    session = requests.session()
    headers = {'Accept':'*/*',
                'Accept-Encoding':'gzip, deflate',
                'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,en-GB;q=0.2',
                'cache-control':'no-cache',
                # 'Content-Length':'105',
                'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
                # 'Cookie':'s=fs311zsufz; bid=f507d90c8e6824d45daf940d93ff2766_ifffwmfh;'
                #          ' snbim_minify=False; last_account=yanheven%40qq.com;'
                #          ' xq_a_token=138a2f04de6b9d0bafb7cf63b0e45cf14e9c28e4;'
                #          ' xq_r_token=e3e63e30d7452591c0237b3f2cdb5e89c597aca2;'
                #          ' __utmt=1; __utma=1.480589474.1444140112.1447046099.'
                #          '1447049023.8; __utmb=1.1.10.1447049023; __utmc=1; __'
                #          'utmz=1.1444140112.1.1.utmcsr=(direct)|utmccn=(direct)|'
                #          'utmcmd=(none); Hm_lvt_1db88642e346389874251b5a1eded6e3='
                #          '1446344992; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1447049024',
                'Host':'xueqiu.com',
                'Origin':'http://xueqiu.com',
                'Proxy-Connection':'keep-alive',
                # 'Referer':'http://xueqiu.com/yanhaven',
                'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
                'X-Requested-With':'XMLHttpRequest'
              }
    body = {}
    body['headers'] = headers
    body['data'] = data
    try:
        res = session.get('http://xueqiu.com/service/csrf?api=http%3A%2F%2Fxueqiu.com%2Fuser%2Flogin', headers=headers)
        print(res)
        # print(res.content)
        res = session.get(pre_url+time_now, headers=headers)
        print(res)
        print(res.content)
        res = session.post( login_url, headers=headers,data=data)
        print(res)
        print(res.content)
    except Exception as e:
        print(e)

    rebalance = {'cube_symbol':'ZH698696',
                'cash':'61.81',
                'segment':'True',
                'holdings':[{"stock_id":1023259,"weight":1.05,"segment_name":"ETF","segment_id":3481903,
                     "stock_name":"H股ETF","stock_symbol":"SH510900","segment_color":"#e84e24",
                     "proactive":False,"volume":0.00980672,"textname":"H股ETF(SH510900)","url":"/S/SH510900",
                     "price":1.067,"percent":0.19,"flag":1},{"stock_id":1023221,"weight":1.14,
                     "segment_name":"ETF","segment_id":3481903,"stock_name":"50ETF","stock_symbol":"SH510050",
                     "segment_color":"#e84e24","proactive":False,"volume":0.00448683,"textname":"50ETF(SH510050)",
                     "url":"/S/SH510050","price":2.532,"percent":1.32,"flag":1},{"stock_id":1001086,"weight":27,
                    "segment_name":"银行","segment_id":3678047,"stock_name":"平安银行","stock_symbol":"SZ000001",
                    "segment_color":"#5594e7","proactive":True,"volume":0.04081696,"textname":"平安银行(SZ000001)",
                    "url":"/S/SZ000001","price":12.94,"percent":4.44,"flag":1},{"stock_id":1001089,"weight":2,
                    "segment_name":"房地产","segment_id":3680301,"stock_name":"世纪星源","stock_symbol":"SZ000005",
                    "segment_color":"#d9633b","proactive":True,"volume":0.00939255,"textname":"世纪星源(SZ000005)",
                    "url":"/S/SZ000005","price":10.61,"percent":6.63,"flag":1},{"code":"SZ000061","name":"农产品",
                    "enName":None,"hasexist":None,"flag":1,"type":None,"current":15.77,"chg":0.27,"percent":"1.74",
                    "stock_id":1001135,"ind_id":100015,"ind_name":"商业贸易","ind_color":"#bc8e58",
                    "textname":"农产品(SZ000061)","segment_name":"商业贸易","weight":7,"url":"/S/SZ000061",
                    "proactive":True,"price":"15.77"}],
                'comment':'a'}
    # rebalance=(urllib.urlencode(rebalance))
    data = {'symbol':'ZH698696',
              'name':'27000',
              'description':'ffff21380assss5620a'}
    try:
        res = session.get('http://xueqiu.com/p/update?action=info&symbol=ZH698696',headers=headers)
        print(res)
        res = session.post(update_url,data=data,headers=headers)
        print(res)
        print(res.content)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    get_xueqiu_login_session()