#!/usr/bin/env python3
# _*_ codding = utf-8 _*_
# author : k3vi
from handle import get
import re


def get_page_num(): # get the number of the page
	frist_page = get('http://wooyun.org/bugs/')
	try:
		page_num = re.findall(r'共.*条纪录, (\d{4,8}) 页', frist_page)[0]
		page_num = int(page_num)
		print(page_num)
	except Exception as e:
		print(e)


def bug_urls(url):
	"""

	:return: urls list
	"""
	page = get(url)
	x = re.findall(r'<a href="/bugs/(wooyun-\d{4}-\d{7})">(.{0,50})</a>',page)
	print(x)

bug_urls('http://wooyun.org/bugs/page/2')