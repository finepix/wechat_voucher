import requests

# domain = 'http://api.shouqiev.com'
# url = domain + '/share/shareRedEnvelope.json?orderId=180807144928943MOEDW32&from=singlemessage '

headers = {
    'Host': 'api.shouqiev.com',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; vivo X9 Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044203 Mobile Safari/537.36 MicroMessenger/6.6.7.1321(0x26060739) NetType/WIFI Language/zh_CN',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,image/wxpic,image/sharpp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,en-US;q=0.8',
}

# cookies = {
#     'a22bccc7460344a423a03389c1f5587c': '2628c24a68ee413184645001b62ac25c',
#     'Hm_lvt_93a9e137393fca3dd0fcf57a44be5bbc': '1533354673,1533354735,1533355134,1533355504',
#     'Hm_lpvt_93a9e137393fca3dd0fcf57a44be5bbc': '1533641627'
# }

cookies = {
    'a22bccc7460344a423a03389c1f5587c': '2628c24a68ee413184645001b62ac25c'
}


def open_url(url):
    s = requests.session()
    rs = s.get(url, headers=headers, cookies=cookies)
    print(rs.text)


if __name__ == '__main__':

    ss = requests.session()
    r = ss.get(url, headers=headers, cookies=cookies)
    print(r.text)

