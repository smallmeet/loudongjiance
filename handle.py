#!/usr/bin/env python3
# _*_ codding = utf-8 _*_
# author : k3vi
# handle HTTP request
import urllib.request
import urllib.parse


def get(url):  # 发送get请求，返回网页内容
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'
    headers = {"User-Agent": user_agent}
    try:
        req = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(req)
        page = response.read().decode("UTF8")
        return page
    except Exception as e:
        print(e)


def post(url):  # 发送post请求，返回网页内容
    user_agent = "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko"
    try:
        req = urllib.request.Request(url)
        req.add_header("User-Agent", user_agent)
        f = urllib.request.urlopen(req)
        page = f.read().decode("UTF8")
        return page
    except Exception as e:
        print(e)


def deal_tags():  # 处理tags.txt，返回一个关键字列表
    try:
        with open('./tags.txt', 'rt') as f:
            tags = f.readlines()
    except Exception as e:
        print(e)
    r_tags = []
    for tag in tags:
        tag = to_str(tag)
        r_tags.append(tag.strip())
    return r_tags


def to_str(bytes_or_str):     # 接受str和bytes，并总返回str
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value
