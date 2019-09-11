#basic code for weixin mp check
#coding:utf-8
import tornado.escape
import tornado.web

from wechat_sdk import WechatConf

conf = WechatConf(
    token='weixin', # 你的公众号Token
    appid='wx74d10c0aee9723d7', # 你的公众号的AppID
    appsecret='a32c180bdf62d80ae29c28f2903f9c15', # 你的公众号的AppSecret
    encrypt_mode='normal',  # 可选项：normal/compatible/safe，分别对应于 明文/兼容/安全 模式
    encoding_aes_key='tImDoypAVjBW7DEECBwqqQM9cdyYfPMB8qbOGgHLETc'  # 如果传入此值则必须保证同时传入 token, appid
)

from wechat_sdk import WechatBasic
wechat = WechatBasic(conf=conf)

class WX(tornado.web.RequestHandler):
    def get(self):
        print("receive check get requests... ")
        print(self.get_arguments)
        signature = self.get_argument('signature', 'default')
        timestamp = self.get_argument('timestamp', 'default')
        nonce = self.get_argument('nonce', 'default')
        echostr = self.get_argument('echostr', 'default')
        if signature != 'default' and timestamp != 'default' and nonce != 'default' and echostr != 'default' \
                and wechat.check_signature(signature, timestamp, nonce):
            self.write(echostr)
        else:
            self.write('Not Open')