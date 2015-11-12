__author__ = 'evan'
LOGIN_URL = 'https://stock.pingan.com.cn/pa/newstock/webTrade/cgi-bin/trade/Login?logout=true'
INDEX_URL = 'https://stock.pingan.com.cn/pa/newstock/webTrade/trade/index.html?logout=true'
LOCK_URL = 'https://stock.pingan.com.cn/pa/newstock/webTrade/trade/index.html?logout=true'
TRANSACT_URL = 'https://stock.pingan.com.cn/pa/newstock/webTrade/cgi-bin/trade/Trade'

ACCOUNT = ''
PASSWORD = ''
BUY_BODY = {'SH_TRD_ID':'UB',
            'SZ_TRD_ID':'2B',
            'SECU_CODE':'510050',
            'QTY':'1',
            'PRICE':'2.473',
            'hightstop':'2.7540',
            'lowstop':'2.2540',
            'funcNo':'001',
            'component_id':'SUBMIT',
            'isCompress':'false',
            'ACCOUT':'10%7CA264639903',
            'random':'0.2880477933213115',
            'return':'AVAILABLE%3AAVAILABLE%7CMAXNUM%3ASHARE_QTY%7CMAXNUMPER%3A%7CQTY%3A%7Ctable1%3A',
            'MAXNUM':'0',
            'AVAILABLE':'0.96',
            'SECU_NAME':'50ETF',}


SELL_BODY = {'SH_TRD_ID':'US',
             'SZ_TRD_ID':'2S',
             'SECU_CODE':'510050',
             'QTY':'100',
             'PRICE':'2.753',
             'hightstop': '2.7540',
             'lowstop':'2.2540',
             'allch': '',
             'funcNo':'001',
             'component_id':'SUBMIT',
             'SECU_STATUS':'0',
             'isCompress':'false',
             'ACCOUT':'10%7CA264639903',
             'random':'0.830732898786664',
             'return':'MAXNUM%3ASHARE_QTY%7CMAXNUMPER%3A%7CQTY%3A%7Ctable1%3A',}

HISTORY_BODY = {'return':'table1%3A',
                'random':'0.08271421026438475',
                'component_id':'',
                'isCompress':'false',
                'END_DATE':'2015-11-12',
                'funcNo':'006',
                'BEGIN_DATE':'2015-11-01'}

# SELL_BODY = {'TRD_ID':'0S',
#              'SECU_CODE':'510050',
#              'PRICE':'2.753',
#              'QTY':'100',
#              'hightstop': '2.7540',
#              'lowstop':'2.2540',
#              'allch': '',
#              'funcNo':'001',
#              'component_id':'SUBMIT',
#              'SECU_STATUS':'0',
#              'isCompress':'false',
#              'ACCOUT':'10%7CA264639903',
#              'random':'0.830732898786664',
#              'return':'MAXNUM%3ASHARE_QTY%7CMAXNUMPER%3A%7CQTY%3A%7Ctable1%3A',
#              'SEAT':'',
#              'FLAG':'false',
#              'SHARE_AVL':'100',}
#
# BUY_BODY = {'TRD_ID':'0B',
#             'SECU_CODE':'510050',
#             'PRICE':'2.473',
#             'QTY':'1',
#             'hightstop':'2.7540',
#             'lowstop':'2.2540',
#             'allch':'',
#             'funcNo':'001',
#             'component_id':'','SECU_STATUS':'0',
#             'isCompress':'false',
#             'ACCOUT':'10%7CA264639903',
#             'random':'0.08871170226484537',
#             'return':'AVAILABLE%3AAVAILABLE%7CMAXNUM%3ASHARE_QTY%7CMAXNUMPER%3A%7CQTY%3A%7Ctable1%3A',
#             'MAXNUM':'0',
#             'TREE_ID':'1000',
#             'AVAILABLE':'0.96',
#             'SECU_NAME':'50ETF',}

LOCK_BODY = {'isCompress': 'false',
             'random': '0.4553212048485875',
             'isLocked': 'false',
             'funcNo': '103'}

LOGIN_BODY = {'password': PASSWORD,
              'mac': '',
              'hard': '',
              'isSafe': 'false',
              'input_content': 'Z',
              'branch_no': '3099',
              'fund_account': ACCOUNT,
              'ticket': '1509',
              'x': '0',
              'y': '0'}

SELL2_BODY= {'funcNo':'004',
               'random':'0.363096522167325',
               'isCompress':'false'}

WITHDRAW_BODY = {'MARKET':'10',
                 'ORDER_ID':'70550929',
                 'component_id':'',
                 'return':'table1%3A',
                 'funcNo':'003',
                 'random':'0.6700310669839382',
                 'isCompress':'false'}

WITHDRAW2_BODY = {'funcNo':'005',
                  'random':'0.183338460046798',
                  'queryType':'cancel',
                  'isCompress':'false'}

LOGIN_2 ={'isCompress':'false',
          'random':'0.47174918465316296',
          'funcNo':'048',}

LOGIN_3 = {'isCompress':'false',
          'random':'0.3738884483464062',
          'funcNo':'100',}


# #buy
# allch:
# MAXNUM:0
# random:0.7607198287732899
# SECU_CODE:510050
# SECU_NAME:50ETF
# ACCOUT:10%7CA264639903
# component_id:SUBMIT
# isCompress:false
# SECU_STATUS:0
# PRICE:2.473
# AVAILABLE:0.96
# return:AVAILABLE%3AAVAILABLE%7CMAXNUM%3ASHARE_QTY%7CMAXNUMPER%3A%7CQTY%3A%7Ctable1%3A
# hightstop:2.7540
# funcNo:001
# lowstop:2.2540
# SZ_TRD_ID:2B
# SH_TRD_ID:UB
# QTY:1

# #sell
# SH_TRD_ID:US
# PRICE:2.471
# SZ_TRD_ID:2S
# SECU_CODE:510050
# ACCOUT:10%7CA264639903
# SECU_STATUS:0
# random:0.00941555853933096
# isCompress:false
# funcNo:001
# QTY:100
# hightstop:2.7540
# return:MAXNUM%3ASHARE_QTY%7CMAXNUMPER%3A%7CQTY%3A%7Ctable1%3A
# component_id:SUBMIT
# lowstop:2.2540
# allch:
# MAXNUM:100

## query history
# return:table1%3A
# random:0.08271421026438475
# component_id:
# isCompress:false
# END_DATE:2015-11-12
# funcNo:006
# BEGIN_DATE:2015-11-12

# isCompress:false
# random:0.47174918465316296
# funcNo:048
#
# isCompress:false
# random:0.3738884483464062
# funcNo:100
