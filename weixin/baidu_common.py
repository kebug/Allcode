# coding: utf8
'''
    @Author: LCY
    @Contact: lchuanyong@126.com
    @blog: http://http://blog.csdn.net/lcyong_
    @Date: 2018-01-15
    @Time: 19:19
    说明： appid和secretKey为百度翻译文档中自带的，需要切换为自己的
           python2和python3部分库名称更改对应如下：
           httplib      ---->    http.client
           md5          ---->    hashlib.md5
           urllib.quote ---->    urllib.parse.quote
    官方链接：
           http://api.fanyi.baidu.com/api/trans/product/index

'''

import http.client
import hashlib
import json
import urllib
import random


def baidu_translate(content, slan, dlan):
    appid = '20181130000241292'
    secretKey = 'GhaXKfXxYKeoG6318dK5'
    httpClient = None
    myurl = '/api/trans/vip/translate'
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
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        # response是HTTPResponse对象
        response = httpClient.getresponse()
        jsonResponse = response.read().decode("utf-8")  # 获得返回的结果，结果为json格式
        js = json.loads(jsonResponse)  # 将json格式的结果转换字典结构
        # print(js)
        dst = str(js["trans_result"][0]["dst"])  # 取得翻译后的文本结果
        return dst
    except Exception as e:
        return e
    finally:
        if httpClient:
            httpClient.close()


def translate(content):
    slan = None
    dlan = None
    tmp = content.encode("utf-8")
    if tmp.isalpha():
        slan = "en"
        dlan = "zh"
    else:
        slan = "zh"
        dlan = "en"
    result = baidu_translate(content, slan, dlan)
    return result
