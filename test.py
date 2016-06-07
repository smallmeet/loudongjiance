#!/usr/bin/env python3
# _*_ codding = utf-8 _*_
# author : k3vi
from handle import get, deal_tags
import re


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
                return r_i
    return r_i


def matching_keywords(keywords):  # 处理关键字
    key_str = ''
    for key in keywords:
        if keywords[len(keywords) - 1] != key:
            key_str += key + '|'
        else:
            key_str += key
    return key_str


def get_bug_url(bugs):  # 把编号合成url
    bug_url_list = []
    for bug in bugs:
        tmp = 'http://wooyun.org/bugs/%s' % bug
        bug_url_list.append(tmp)
    return bug_url_list


def get_bug_page(urls):
    tags = deal_tags()
    keys = matching_keywords(tags)
    re_key = re.compile(keys)  # 关键字编译成re
    for url in urls:
        page = get(url)
        tmp_list = []
        x = re.search(re_key, page)
        if x:
            title = re.findall(r'<title> (.{10,80}) \| (WooYun-\d{4}-\d{6}) \| WooYun.org </title>', page)  # 获取漏洞名称，编号
            time = re.findall(r'提交时间：\s*(2016-\d{2}-\d{2})', page)  # 获取漏洞发布时间
            # --> 此处内容为存储到数据库中的内容
            tmp_list.append(title[0][0])    # 漏洞名称
            tmp_list.append(title[0][1])    # 漏洞编号
            tmp_list.append('http://wooyun.org/bugs/%s' % title[0][1].lower())  # 漏洞链接
            tmp_list.append(time[0])    # 漏洞发布时间
            # <-- 此处内容为存储到数据库中的内容
            print(tmp_list)


def main():
    bugs_id = handle_pages('wooyun-2016-0216682')
    urls = get_bug_url(bugs_id)
    get_bug_page(urls)


if __name__ == '__main__':
    main()