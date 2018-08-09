import itchat
import itchat.content as ct
from bs4 import BeautifulSoup
from wechat_voucher import open_url_shouqiev as ous


domain = "api.shouqiev.com"                 # 用来判断是否为gofun的券


@itchat.msg_register(ct.INCOME_MSG)
def msg_rq(msg):
    if hasattr(msg, 'MsgType'):
        if msg.MsgType == 1:                # 普通的文字
            print(msg.text)
        elif msg.MsgType == 49:             # 网页链接
            print(msg.Url)
            url = msg.Url
            if domain in url:               # 拉取gofun的链接
                ous.open_url(msg.Url)       # 打开该链接
    return


if __name__ == '__main__':
    itchat.auto_login()
    itchat.run()
