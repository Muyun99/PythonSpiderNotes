import requests
from urllib import parse
from urllib import request
import json
import time
import random
import hashlib


def postDemo1(i):
    
    # 构造ts和salt
    ts = int(time.time() * 1000)                        # 由于网页是用的js的时间戳(毫秒)跟python(秒)的时间戳不在一个级别，所以需要*1000
    salt = str(ts + random.randint(1, 10))
    # 构造sign
    client = "fanyideskweb"
    FlowerStr = "@6f#X3=cCuncYssPsuRUE"
    sign = hashlib.md5(
        (client + i + salt + FlowerStr).encode('utf-8')).hexdigest()
    # 构造bv
    bv = "a4da7fd2fcb0c879a8b1e37b497afb19"             # bv = n.md5(navigator.appVersion)

    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    formdata = {
        "i": i,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": salt,
        "sign": sign,
        "ts": ts,
        "bv": bv,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_CLICKBUTTION"
    }
    
    headers = {
        "Cookie": "OUTFOX_SEARCH_USER_ID_NCOO=873332859.951251; OUTFOX_SEARCH_USER_ID=\"1211099747@10.169.0.84\"; _ntes_nnid=dde89ec27769f72c83047c87cbaa88c9,1555911538889; JSESSIONID=aaa3JUBVFr_8o6hDgZDRw; SESSION_FROM_COOKIE=www.google.com; UM_distinctid=16addccbdbe3b6-0295fe0270939b-353166-384000-16addccbdbf3d2; ___rl__test__cookies=1558509874405",
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
    }

    translate_result = requests.post(url=url,data=formdata,headers=headers).json()
    #print(translate_result)
    print("翻译后的结果是:%s" % translate_result["translateResult"][0][0]['tgt'])


if __name__ == '__main__':
    while True:
        i = input("请输入你要翻译的文字('quit':退出):  ").strip()
        if i == 'quit':
            break;
        else:
            postDemo1(i)