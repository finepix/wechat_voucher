import itchat
import itchat.content as ct
from wechat_voucher import open_url_shouqiev as ous


@itchat.msg_register(ct.INCOME_MSG)
def msg_rq(msg):
    if msg.MsgType == 1:                # 普通的文字
        print(msg.text)
    elif msg.MsgType == 49:             # 网页链接
        print(msg.Url)
        ous.open_url(msg.Url)           # 打开该链接
    return


if __name__ == '__main__':
    itchat.auto_login()
    itchat.run()
