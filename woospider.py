#!/usr/bin/env python3
# _*_ codding = utf-8 _*_
# author : k3vi
from handle import get, matching_keywords
from mysqldb import getkeyWord, wooyun_insert, wooyun_last, wooyun_last_update
import re
import sys


def get_bug_id(url):  # 获取漏洞的编号
    page = get(url)
    x = re.findall(r'<a href="/bugs/(wooyun-\d{4}-\d{7})">.*</a>', page)
    return x


def handle_pages(last_bugs_id):  # 页面中所有未处理的漏洞编号
    r_i = []
    for x in range(1, 10):
        url = url = 'http://wooyun.org/bugs/page/%d' % x
        bugs_id = get_bug_id(url)
        for r_id in bugs_id:
            if r_id != last_bugs_id:
                r_i.append(r_id)
            elif r_id == last_bugs_id:
                if bugs_id[0] != last_bugs_id:
                    wooyun_last_update(r_i[0])
                else:
                    sys.exit()
            return r_i
    return r_i


def get_bug_url(bugs):  # 把编号合成url
    bug_url_list = []
    for bug in bugs:
        tmp = 'http://wooyun.org/bugs/%s' % bug
        bug_url_list.append(tmp)
    return bug_url_list


def get_bug_page(urls):
    keys = matching_keywords()
    re_key = re.compile(keys)  # 关键字编译成re
    for url in urls:
        page = get(url)
        tmp_list = []
        x = re.search(re_key, page)
        if x:
            title = re.findall(r'<title> (.{10,80}) \| (WooYun-\d{4}-\d{6}) \| WooYun.org </title>', page)  # 获取漏洞名称，编号
            time = re.findall(r'提交时间：\s*(2016-\d{2}-\d{2})', page)  # 获取漏洞发布时间
            # --> 此处内容为存储到数据库中的内容
            keyword = x.group()  # 关键字
            bug_name = title[0][0]  # 漏洞名称
            bug_id = title[0][1]  # 漏洞编号
            bug_time = time[0]  # 漏洞发布时间
            print(keyword,bug_name,bug_id,bug_time)
            wooyun_insert(bug_name, bug_id, bug_time, keyword)
            # <-- 此处内容为存储到数据库中的内容
            print(tmp_list)


def main():
    last_id = wooyun_last()
    bugs_id = handle_pages(last_id) # 获取最后一条id        
    urls = get_bug_url(bugs_id)
    get_bug_page(urls)


if __name__ == '__main__':
    main()
