'''
Created on Dec 15, 2014

@author: hyphen
'''
import requests

session=requests.session()
data = {
        'email': '344736086@qq.com',
        'password': 'yhflmq',
        'webrequest': 'true'
    }
recieve=session.post('http://www.coursera.com', data)
session.get("https://class.coursera.org/sdn-002/lecture")
