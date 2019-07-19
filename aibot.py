#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from uuid import uuid4
import hashlib
from urllib import parse
import time
import random
import string
import requests



def send_moli(msg=''):
    if msg=='/moli' or msg=='/ai':
        msg = '你好'
    else:
        msg = msg.replace('/moli ','')
    moli_data = {
        "question": msg,
        "api_key": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "api_secret": "xxxxxxxxx"
    }
    moli_api_url = 'http://i.itpk.cn/api.php'
    res = requests.post(moli_api_url, data=moli_data)
    if msg == '笑话':
        result = json.loads(res.text.strip()[1:])
        return '*' + result['title'] + '*\n' + result['content']
    if msg == '观音灵签':
        result = json.loads(res.text.strip()[1:])
        return '*'+result['type'] + '*\n' + result['haohua'] + '\n签语：' + result['qianyu'] + '\n释义：' + result['shiyi'] + '\n解签：' + result['jieqian']
    if msg == '月老灵签':
        result = json.loads(res.text.strip()[1:])
        return '*' + result['type'] + '*\n' + result['haohua'] + '\n释义：' + result['shiyi'] + '\n解签：' + result['jieqian']
    if msg == '财神爷灵签':
        result = json.loads(res.text.strip()[1:])
        return '*' + result['type'] + '*\n' + '签语：' + result['qianyu'] + '\n财务：' + result['cwyj'] + '\n谋事：' + result['moushi'] + '\n求财：' + result['qiucai'] + '\n婚姻：' + result['hunyin'] + '\n交易：' + result['jiaoyi'] + '\n失物：' + result['shiwu'] + '\n疾病：' + result['jibin'] + '\n功名：' + result['gongming'] + '\n事业：' + result['shiye'] + '\n运途：' + result['yuntu'] + '\n合伙做生意：' + result['hhzsy'] + '\n解签：' + result['jieqian'] + '\n解说：' + result['jieshuo'] + '\n结果：' + result['jieguo']
    return res.text.strip()[1:]


def get_nlp_textchat(msg='', userId='test'):
    if msg == '/ai':
        msg = '你好'
    else:
        msg = msg.replace('/ai ','')
    app_id = 'xxxxxxxx'
    app_key = 'xxxxxxxxxxxxxxx'
    URL = 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat'
    nonce_str = ''.join(random.sample(
        string.ascii_letters + string.digits, random.randint(10, 16)))
    time_stamp = int(time.time())  # 时间戳
    params = {
        'app_id': app_id,  # 应用标识
        'time_stamp': time_stamp,  # 请求时间戳（秒级）
        'nonce_str': nonce_str,  # 随机字符串
        'session': userId,  # 会话标识
        'question': msg  # 用户输入的聊天内容
    }
    # 签名信息
    uri_str = parse.urlencode(sorted(params.items()), encoding="UTF-8")
    sign_str = '{}&app_key={}'.format(uri_str, app_key)
    # print('sign =', sign_str.strip())
    hash_md5 = hashlib.md5(sign_str.encode("UTF-8"))
    params['sign'] = hash_md5.hexdigest().upper()
    resp = requests.get(URL, params=params)
    if resp.status_code == 200:
        # print(resp.text)
        content_dict = resp.json()
        if content_dict['ret'] == 0:
            data_dict = content_dict['data']
    return data_dict['answer']


if __name__ == '__main__':
    data = get_nlp_textchat('你好')
    print(data)
    data = send_moli('财神爷灵签')
    print(data)