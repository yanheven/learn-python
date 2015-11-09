#_*_ coding: UTF-8 _*_
__author__ = 'evan'
import json
import requests
import time

from const import headers
import login


origin_hold = ''

def rebalance(body):
    rebalance_url = 'http://xueqiu.com/cubes/rebalancing/create.json'
    session = login.get_session()
    headers['Referer'] = 'http://xueqiu.com/p/update?action=holdings&symbol=ZH698696'
    rebalance_res = session.post(rebalance_url, headers=headers,
                             data=body)
    print('rebalance', rebalance_res)



def get_hold(url):
    # url = 'http://xueqiu.com/P/ZH010389'
    res = requests.get(url, headers=headers)
    print('get change', res)
    holdings = res.content
    holdings = holdings.split('SNB.cubeInfo = ')[1].split('SNB.cubePieData')[0]
    holdings = json.loads(holdings,encoding='utf-8').get('view_rebalancing').get('holdings')
    # print(holdings)
    hold = {}
    holdings_str = '''['''
    cash = 100
    sorted(holdings, key=lambda x: x['stock_id'])
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
    return hold_body

def follow():
    other_url = 'http://xueqiu.com/P/ZH010389'
    other_hold = get_hold(other_url)
    global origin_hold
    if not origin_hold:
        origin_hold = json.dumps(other_hold)
    elif origin_hold != json.dumps(other_hold):
        other_hold['cube_symbol'] = 'ZH698696'
        other_hold['segment'] = 'true'
        rebalance(other_hold)
        return True
    return False



rebalance_url = 'http://xueqiu.com/cubes/rebalancing/create.json'
update_url = 'http://xueqiu.com/cubes/update.json'
session = login.get_session()
# headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) Apple'
#                         'WebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93'
#                         ' Safari/537.36'
#            }

update_body = {'symbol':'ZH698696',
               'name':'27000',
               'description':'ffff21380assss5620a'}


# headers['Referer'] = 'http://xueqiu.com/p/update?action=info&symbol=ZH698696'
# update_res = session.post(update_url, headers=headers, data=update_body)
# print('update', update_res)

rebalance_body = {'cube_symbol':'ZH698696',
                  'cash':'65.95',
                  'segment':'true',
                  # 'holdings':'[{"stock_id":1001089,"weight":2,"segment_name":"房地产","segment_id":3680301,"stock_name":"世纪星源","stock_symbol":"SZ000005","segment_color":"#d9633b","proactive":true,"volume":0.00187851,"textname":"世纪星源(SZ000005)","url":"/S/SZ000005","price":10.61,"percent":6.63,"flag":1},'
                  #             '{"stock_id":1001135,"weight":7,"segment_name":"商业贸易","segment_id":3680316,"stock_name":"农产品","stock_symbol":"SZ000061","segment_color":"#bc8e58","proactive":true,"volume":0.00442349,"textname":"农产品(SZ000061)","url":"/S/SZ000061","price":15.77,"percent":1.74,"flag":1},'
                  #             '{"stock_id":1001086,"weight":27,"segment_name":"银行","segment_id":3678047,"stock_name":"平安银行","stock_symbol":"SZ000001","segment_color":"#5594e7","proactive":false,"volume":0.02079354,"textname":"平安银行(SZ000001)","url":"/S/SZ000001","price":12.94,"percent":4.44,"flag":1},'
                  #             '{"stock_id":1023221,"weight":10,"segment_name":"ETF","segment_id":3481903,"stock_name":"50ETF","stock_symbol":"SH510050","segment_color":"#e84e24","proactive":true,"volume":0.00448683,"textname":"50ETF(SH510050)","url":"/S/SH510050","price":2.532,"percent":1.32,"flag":1},'
                  #             '{"stock_id":1023259,"weight":1.05,"segment_name":"ETF","segment_id":3481903,"stock_name":"H股ETF","stock_symbol":"SH510900","segment_color":"#e84e24","proactive":false,"volume":0.00980672,"textname":"H股ETF(SH510900)","url":"/S/SH510900","price":1.067,"percent":0.19,"flag":1}]',
                  'comment':'跟手哥吃饭的',
                  'holdings':'''[{"stock_id":1001089,"weight":10,"segment_name":"房地产"},{"stock_id":1001086,"weight":13,"segment_name":"银行","segment_id":3678047,"stock_name":"平安银行","stock_symbol":"SZ000001","segment_color":"#5594e7","proactive":true,"volume":0.02079354,"textname":"平安银行(SZ000001)","url":"/S/SZ000001","price":12.94,"percent":4.44,"flag":1},{"stock_id":1023221,"weight":10,"segment_name":"ETF","segment_id":3481903,"stock_name":"50ETF","stock_symbol":"SH510050","segment_color":"#e84e24","proactive":false,"volume":0.03935821,"textname":"50ETF(SH510050)","url":"/S/SH510050","price":2.532,"percent":1.32,"flag":1},{"stock_id":1023259,"weight":1.05,"segment_name":"ETF","segment_id":3481903,"stock_name":"H股ETF","stock_symbol":"SH510900","segment_color":"#e84e24","proactive":false,"volume":0.00980672,"textname":"H股ETF(SH510900)","url":"/S/SH510900","price":1.067,"percent":0.19,"flag":1}]'''
                  #  'holdings':holdings
                  }

if __name__ == '__main__':
    while True:
        if follow():
            break
        time.sleep(1)