'''
例：将apple从英文翻译成中文：
请求参数：
q=apple
from=en
to=zh
appid=2015063000000001
salt=1435660288
平台分配的密钥: 12345678
生成sign：
>拼接字符串1
拼接appid=2015063000000001+q=apple+salt=1435660288+密钥=12345678
得到字符串1 =2015063000000001apple143566028812345678
>计算签名sign（对字符串1做md5加密，注意计算md5之前，串1必须为UTF-8编码）
sign=md5(2015063000000001apple143566028812345678)
sign=f89f9594663708c1605f3d736d01d2d4
完整请求为：
http://api.fanyi.baidu.com/api/trans/vip/translate?q=apple&from=en&to=zh&appid=2015063000000001&salt=1435660288&sign=f89f9594663708c1605f3d736d01d2d4
也可以使用POST方法传送需要的参数。
'''
import hashlib
import urllib
import random
import requests


def baidu_translate(content,slan,dlan):
    appid = '20181130000241292'
    secretKey = 'GhaXKfXxYKeoG6318dK5'
    myurl = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    q = content
    fromLang = slan  # 源语言
    toLang = dlan  # 翻译后的语言
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
        q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign

    try:
        response = requests.get(myurl)
        return response.text
    except Exception as e:
        return e

def translate(content):
        slan = None
        dlan = None
        if content.encode("utf-8").isalpha():
            slan = "en"
            dlan = "zh"
        else:
            slan = "zh"
            dlan = "en"
        result = baidu_translate(content,slan,dlan)
        return result

if __name__ == '__main__':
    print(translate("good"))
    print(translate("中国"))