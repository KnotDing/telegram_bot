import json

import requests

# 翻译函数，word 需要翻译的内容
def translate(word):
    # 有道词典 api
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
    # 传输的参数，其中 i 为需要翻译的内容
    key = {
        'type': "AUTO",
        'i': word,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "ue": "UTF-8",
        "action": "FY_BY_CLICKBUTTON",
        "typoResult": "true"
    }
    # key 这个字典为发送给有道词典服务器的内容
    response = requests.post(url, data=key)
    # 判断服务器是否相应成功
    if response.status_code == 200:
        # 然后相应的结果
        return response.text
    else:
        print("有道词典调用失败")
        # 相应失败就返回空
        return None

def get_reuslt(repsonse):
    # 通过 json.loads 把返回的结果加载成 json 格式
    result = json.loads(repsonse)
    result_ = '输入的词为：' + result['translateResult'][0][0]['src'] + '\n'
    result_ += '翻译结果为：' + result['translateResult'][0][0]['tgt']
    return result_

def fanyi(word=''):
    if word=='/fanyi':
        result_word = '本指令调用有道词典的API进行翻译，可达到以下效果：\n'
        result_word += '外文-->中文\n'
        result_word += '中文-->英文\n'
    else:
        list_trans = translate(word.replace('/fanyi ',''))
        result_word = get_reuslt(list_trans)
    return result_word

if __name__ == '__main__':
    data = fanyi()
    print(data)