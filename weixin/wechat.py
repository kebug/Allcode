import tornado.web
import tornado.options
import tornado.httpserver
import tornado.ioloop
import hashlib
from tornado.web import RequestHandler
from tornado.options import options,define
import xmltodict
import time
from baidu_common import translate

WECHAT_TOKEN = "kevin"

define("port", default=80, type=int, help="")


class WechatHandle(RequestHandler):
    def prepare(self):
        signature = self.get_argument("signature")
        timestamp = self.get_argument("timestamp")
        nonce = self.get_argument("nonce")
        # echostr = self.get_argument("echostr")
        tmp = [WECHAT_TOKEN, timestamp, nonce]
        tmp.sort()
        tmp_str = "".join(tmp)
        real_signature = hashlib.sha1(tmp_str.encode("utf-8")).hexdigest()
        if signature != real_signature:
            self.write("error")

    # 对接微信服务器
    def get(self):
        echostr = self.get_argument("echostr")
        self.write(echostr)

    def post(self):
        xml_data = self.request.body
        dict_data = xmltodict.parse(xml_data)
        msg_type = dict_data["xml"]["MsgType"]
        if msg_type == "text":
            # 根据content内容进行相应小功能的实现
            content = dict_data["xml"]["Content"]
            content_type = content.split(" ")[0]
            content_msg = content.split(" ")[1]
            if content_type == "1":
                # 调用百度翻译
                result_content = translate(content_msg)
                resp_data = {
                    "xml": {
                        "ToUserName": dict_data["xml"]["FromUserName"],
                        "FromUserName": dict_data["xml"]["ToUserName"],
                        "CreateTime": int(time.time()),
                        "MsgType": "text",
                        "Content": result_content,
                    }
                }
                self.write(xmltodict.unparse(resp_data))
            elif content_type == "2":
                # 调用百度垂直翻译
                pass
            else:
                pass

def main():
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        [
            (r"/wechat",WechatHandle)
        ]
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
