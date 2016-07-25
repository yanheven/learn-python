#!/usr/bin/env python
#  -*- coding: utf-8 -*-
__author__ = 'evan'
import requests
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool as TreadPool
import queue
import threading
import time


base_url = 'http://write.epubit.com.cn/'

text = ''
headers = {'Cookie': '__RequestVerificationToken=679wg1IgLGexZy97oNxoh0aXxBfZ9x21WvSCCJQi_P4--4rE0bdgVdmeSOzQMNZkhTK6UObru6EkUAbTH9yn7Qb0SLxJ7oP5kTHvcsxSQgY1; .ASPXAUTH=B3AE75BF31D9E48535CE58F8FDD6738176DCD9867CD79FE207D0BF0B22A760F1900406A1FBE17A3F81BB1A8826192537ED9A7247800D0F61BB4C403FAECD6703C4B76BBDE098B65324FCB428DA9FE6999AEDBD6AFED797ADE8F0CF30113E540C4F6D7C3E1742C7AAB7CDC0ED612F9C93'}

def get_title(paras):
    url, q = paras
    global title_queue
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        try:
            soup = BeautifulSoup(resp.content, from_encoding='utf-8')
        except Exception as e:
            print(e)
            print(resp.content)
        else:
            title_name = soup.title.string
            line = title_name + ' ' + url + '\n'
            # print(line)
            q.put(line)

class Consumer(threading.Thread):
    def __init__(self, title_q):
        self.q = title_q

    def run(self):
        amount = 0
        while True:
            time.sleep(5)
            new_amount = self.q.qsize()
            if new_amount == amount:
                break
        line = ''
        while self.q.qsize():
            line += self.q.get




if __name__ == '__main__':
    q = queue.Queue()
    pool = TreadPool(20)
    pool.map(get_title, [[base_url + str(i), q] for i in range(100, 1500)])
    pool.close()
    pool.join()
    line = ''
    print(q.qsize())
    while q.qsize():
        line += q.get()
    with open('books100-1500.txt', 'w') as fb:
        fb.write(line)