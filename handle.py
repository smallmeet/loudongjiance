#!/usr/bin/env python3
# _*_ codding = utf-8 _*_
# author : k3vi
# handle HTTP request
import urllib.request


def get(url):
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'
    headers = {'User-Agent': user_agent}
    req = urllib.request.Request(url, headers)
    response = urllib.request.urlopen(req)
    page = response.read().decode('UTF8')
    print(page)
    return page

get("http://www.baidu.com")