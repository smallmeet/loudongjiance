#!/usr/bin/env python3
# _*_ codding = utf-8 _*_
# author : k3vi
# handle HTTP request
import urllib.request
import urllib.parse


def get(url):
	user_agent = 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'
	headers = {'User-Agent': user_agent}
	try:
		req = urllib.request.Request(url, headers=headers)
		response = urllib.request.urlopen(req)
		page = response.read().decode('UTF8')
		return page
	except Exception as e:
		print(e)


def post(url):
	user_agent = 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'
	try:
		req = urllib.request.Request(url)
		req.add_header('User-Agent', user_agent)
		f = urllib.request.urlopen(req)
		page = f.read().decode('utf-8')
		return page
	except Exception as e:
		print(e)
