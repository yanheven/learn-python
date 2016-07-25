# -*- coding: utf-8 -*-
__author__ = 'evan'
import requests
from bs4 import BeautifulSoup
base_url = 'http://write.epubit.com.cn/'
login_url = 'http://write.epubit.com.cn/login'
auth_dict = {'Pasword': 'Zm11cHVi',
             'Email': 'yanheven@qq.com',
             '__RequestVerificationToken' : ''}
text = ''
sess = requests.session()
# sess.get('http://write.epubit.com.cn/Account/Login?ReturnUrl=%2f')
auth_dict['__RequestVerificationToken'] = sess.cookies.get('__RequestVerificationToken')
print(auth_dict)
headers = {'Cookie': '__RequestVerificationToken=679wg1IgLGexZy97oNxoh0aXxBfZ9x21WvSCCJQi_P4--4rE0bdgVdmeSOzQMNZkhTK6UObru6EkUAbTH9yn7Qb0SLxJ7oP5kTHvcsxSQgY1; .ASPXAUTH=B3AE75BF31D9E48535CE58F8FDD6738176DCD9867CD79FE207D0BF0B22A760F1900406A1FBE17A3F81BB1A8826192537ED9A7247800D0F61BB4C403FAECD6703C4B76BBDE098B65324FCB428DA9FE6999AEDBD6AFED797ADE8F0CF30113E540C4F6D7C3E1742C7AAB7CDC0ED612F9C93'}
headers = {'Cookie': '__RequestVerificationToken=679wg1IgLGexZy97oNxoh0aXxBfZ9x21WvSCCJQi_P4--4rE0bdgVdmeSOzQMNZkhTK6UObru6EkUAbTH9yn7Qb0SLxJ7oP5kTHvcsxSQgY1; .ASPXAUTH=B3AE75BF31D9E48535CE58F8FDD6738176DCD9867CD79FE207D0BF0B22A760F1900406A1FBE17A3F81BB1A8826192537ED9A7247800D0F61BB4C403FAECD6703C4B76BBDE098B65324FCB428DA9FE6999AEDBD6AFED797ADE8F0CF30113E540C4F6D7C3E1742C7AAB7CDC0ED612F9C93'}
# ret = sess.post(login_url, data=auth_dict, headers=headers)
# print(ret.content)
for i in range(100, 1500):
    url = base_url + str(i)
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content)
        title_name = soup.title.string
        line = title_name + ' ' + url + '\n'
        text += line
        break
with open('books.txt', 'w') as fb:
    fb.write(text)
