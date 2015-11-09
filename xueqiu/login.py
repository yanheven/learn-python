#_*_ coding: UTF-8 _*_
__author__ = 'evan'
import requests

from const import headers

def get_session():

    login_rul = 'http://xueqiu.com/user/login'
    session = requests.session()
    login_body = {'areacode':'86',
                  'username':'yanheven@qq.com',
                  'password':'60DCCC0E54F96005ECAB40CA9762CB83',
                  'remember_me':'on'}
    login_res = session.post(login_rul, headers=headers, data=login_body)
    print('login',login_res)
    return session