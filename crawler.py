# -*- coding: UTF-8 -*-

'''
サイト内リンク（URL）を収集するクローラ

@author: Takuya_AKIYAMA
'''

import requests
from bs4 import BeautifulSoup

# 対象サイト
target_url = 'https://no1s.biz/'

r = requests.get(target_url)
soup = BeautifulSoup(r.text, 'html.parser')

print('リンク（URL）')
for a in soup.find_all('a'):
    print(a.get('href'))

print('titleタグのテキスト')
for a in soup.find_all('title'):
    print(a.string)
