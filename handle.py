#!/usr/bin/env python3
# _*_ codding = utf-8 _*_
# author : k3vi
# handle HTTP request
import urllib.request


def get(url):
	header_dict = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
	try:
		page = urllib.request.urlopen(url).read()
		pagedecode = page.decode('utf-8')  # decode
	except Exception as e:
		print(e)
	assert isinstance(pagedecode, str)
	print(pagedecode)
	return pagedecode


