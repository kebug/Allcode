import tornado.web
import tornado.options
import tornado.httpserver
import tornado.ioloop
import hashlib
from tornado.web import RequestHandler
from tornado.options import options,define

WECHAT_TOKEN = "kevin"

define("port",default=80,type=int,help="")

class WechatHandle(RequestHandler):
    #对接微信服务器
    def get(self):
        signature = self.get_argument("signature")
        timestamp = self.get_argument("timestamp")
        nonce = self.get_argument("nonce")
        echostr = self.get_argument("echostr")

        tmp_arr = [WECHAT_TOKEN, timestamp, nonce]
        tmp_arr.sort()
        tmp_str = "".join(tmp_arr)
        real_signature = hashlib.sha1(tmp_str.encode("utf-8")).hexdigest()
        if signature == real_signature:
            self.write(echostr)
        else:
            self.write("error")
        self.finish()

def main():
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        [
            (r"wechat",WechatHandle)
        ]
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()