#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
from handle import get, deal_tags
from mysqldb import loudonghezi_insert, loudonghezi_last, loudonghezi_last_update
import re


def get_qid(last_data):                        # 抓取每页的ID并与上次任务对比
    li = []
    for n in range(1, 10):
        url = 'https://www.vulbox.com/board/internet/page/%d' % n
        n_page = get(url)
        soup = bs(n_page, "lxml")
        for item in soup.find_all(href=re.compile('^/bugs/'), class_='btn btn-default btn-check'):
            t = str(item)[49:67]
            if t == last_data:
                return li
            li.append(t)


def get_url():                                  # 获取每个id对应链接
    url_data = []
    for n in get_qid(last_data):
        url_data_ = 'https://www.vulbox.com/bugs/%s' % n
        url_data.append(url_data_)
    return url_data


def get_match():
    ti = []
    ur = []
    date = []
    keyword = []
    for n in get_url():
        n_page = get(n)
        soup = bs(n_page, 'lxml')
        text = soup.find_all(text=re.compile('博客|上海|江苏|xss'), limit=1)
        if text:
            keyword_back = re.search(r'博客|上海|江苏|xss', text[0])
            title = soup.h3.string
            time = soup.find('span', class_='time').string[0:10]
            ti.append(title)
            ur.append(n[28:46])
            date.append(time)
            keyword.append(keyword_back.group(0))
    return ti, ur, date, keyword


def main():
    last_data = 'vulbox-2016-022179'
    x = get_match()
    print(x)
