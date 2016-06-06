#!/usr/bin/env python3
# _*_ codding = utf-8 _*_
# author : k3vi
from handle import get
import re


def bug_urls(url):
    page = get(url)
    x = re.findall(r'<a href="/bugs/(wooyun-\d{4}-\d{7})">.*</a>', page)
    return x


def handle_pages(last_bugs_id):
    r_i = []
    for x in range(1, 10):
        url = url = 'http://wooyun.org/bugs/page/%d'% x
        bugs_id = bug_urls(url)
        for r_id in bugs_id:
            if r_id != last_bugs_id:
                r_i.append(r_id)
            elif r_id == last_bugs_id:
                return r_i
    return r_i



i = handle_pages('wooyun-2016-0216593')
print(len(i))
print(i)