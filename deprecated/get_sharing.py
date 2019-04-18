import itchat
import itchat.content as ct
from wechat_voucher.deprecated import open_url_shouqiev as ous

domain = "api.shouqiev.com"                 # 用来判断是否为gofun的券


# 群聊
@itchat.msg_register(ct.INCOME_MSG, isGroupChat=True)
def msg_group_rc(msg):
    if hasattr(msg, 'MsgType'):
        if msg.MsgType == 1:                # 普通的文字
            print('group:' + msg.text)
        elif msg.MsgType == 49:             # 网页链接
            print('group:' + msg.Url)
            url = msg.Url
            if domain in url:               # 拉取gofun的链接
                ous.open_url(msg.Url)       # 打开该链接
    return


# 个人消息(代码复用，我不知道怎么解决)
@itchat.msg_register(ct.INCOME_MSG)
def msg_personal_rc(msg):
    if hasattr(msg, 'MsgType'):
        if msg.MsgType == 1:                # 普通的文字
            print('personal:' + msg.text)
        elif msg.MsgType == 49:             # 网页链接
            print('personal:' + msg.Url)
            url = msg.Url
            if domain in url:               # 拉取gofun的链接
                ous.open_url(msg.Url)       # 打开该链接
    return


if __name__ == '__main__':
    itchat.auto_login()
    itchat.run()
