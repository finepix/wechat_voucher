#!/usr/bin/env python

# encoding: utf-8
'''
# @Time    : 2019/3/28 20:59
# @Author  : shawn_zhu
# @Site    : 
# @File    : parser.py
# @Software: PyCharm

'''

from bs4 import BeautifulSoup
from wechat_voucher.utils.url_connector import url_connector

class Parser:
    def __init__(self, text):
        self.text = text

    def parse(self):
        self.parse_voucher_and_print()

    def parse_voucher_and_print(self):
        pass


if __name__ == '__main__':
    url = 'http://api.shouqiev.com/share/getJsApiInfoByJsonp.jsonurl=https%3A%2F%2Fapp4.shouqiev.com%2Fdist%2F%23%2FgetBlock%3ForderId%3D190328184028028VW3WBZ1&callback=getShareInfo'
    # url = 'https://app4.shouqiev.com/dist/#/getBlock?orderId=190328184028028VW3WBZ1'

    connector = url_connector()
    connector.open_url_by_get(url)
    print(connector.get_request_result_text())
    # parser = Parser()