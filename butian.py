#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
from handle import get
from mysqldb import butian_insert, butian_last, butian_last_update
import re


def get_qid(last_data):                        # 抓取每页的ID并与上次任务对比
    li = []
    for n in range(1, 3):
        url = 'http://loudong.360.cn/vul/list/page/%d' % n
        n_page = get(url)
        soup = bs(n_page, "lxml")
        for item in soup.find_all('p', class_='list-view'):
            t = str(item.find('a', class_=''))[23:39]
            if t == last_data:
                return li
            li.append(t)


def get_url():                                  # 获取每个id对应链接
    url_data = []
    for n in get_qid(last_data):
        url_data_ = 'http://loudong.360.cn/vul/info/qid/%s' % n
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
        text = soup.find_all(text=re.compile('乐清'), limit=1)
        if text:
            keyword_back = re.search(r'乐清', text[0])
            title = soup.find_all(style=re.compile('font-weight: bold'))[0].string
            time = soup.find('dt', text=re.compile('^20')).string[0:10]
            ti.append(title)
            ur.append(n[35:51])
            date.append(time)
            keyword.append(keyword_back.group(0))
    return ti, ur, date, keyword


def main():
    last_data = 'QTVA-2016-445886'
    x = get_match()
    print(x)
