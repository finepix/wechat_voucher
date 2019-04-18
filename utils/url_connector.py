#!/usr/bin/env python

# encoding: utf-8
'''
# @Time    : 2019/3/28 20:46
# @Author  : shawn_zhu
# @Site    :
# @File    : url_connector.py
# @Software: PyCharm

'''

import requests
from wechat_voucher.deprecated import html_parse


headers = {
        'Host': 'api.shouqiev.com',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; vivo X9 Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044203 Mobile Safari/537.36 MicroMessenger/6.6.7.1321(0x26060739) NetType/WIFI Language/zh_CN',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,image/wxpic,image/sharpp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,en-US;q=0.8',
    }

cookies = {
        'a22bccc7460344a423a03389c1f5587c': '2628c24a68ee413184645001b62ac25c'
    }



class url_connector:
    def __init__(self):
        self._headers = headers
        self._cookies = cookies
        self._session = requests.session()
        self._result = None

    def open_url_by_get(self, url):
        self._result = self._session.get(url, headers=self._headers, cookies=self._cookies, verify=False)

    def get_request_result_text(self):
        return self._result.text

    def parse_result_by_given_parser(self, parser):
        pass
