import json
import urllib
import urllib.request
import hashlib
import base64
import urllib.parse
 
# 此处为快递鸟官网申请的帐号和密码
APP_id = "xxxxxxx"            #更换成自己的id
APP_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"        #更换成自己的key
 
 
def encrypt(logistic_code, app_key):
    """数据内容签名：把(请求内容(未编码)+AppKey)进行MD5加密，然后Base64编码"""
    m = hashlib.md5()
    m.update((logistic_code+app_key).encode("utf8"))
    encode_sign = m.hexdigest()
    data_sign = base64.b64encode(encode_sign.encode(encoding='utf-8'))
    return data_sign
def send_post(url, data):
    """发送post请求"""
    post_data = urllib.parse.urlencode(data).encode('utf-8')
    # 设置请求头
    header = {
        "Accept": "application/x-www-form-urlencoded;charset=utf-8",
        "Accept-Encoding": "utf-8"
    }
    req = urllib.request.Request(url, post_data, header)
    get_data = (urllib.request.urlopen(req).read().decode('utf-8'))
    return get_data
 
 
def get_company(logistic_code, app_id, app_key, url):
    """获取对应快递单号的快递公司代码和名称"""
    data1 = {'LogisticCode': logistic_code}
    d1 = json.dumps(data1, sort_keys=True)
    data_sign = encrypt(d1, app_key)
 
    post_data = {
        'RequestData': d1,
        'EBusinessID': app_id,
        'RequestType': '2002',          # 单号识别接口编码
        'DataType': '2',
        'DataSign': data_sign.decode()
    }
 
    json_data = send_post(url, post_data)
    sort_data = json.loads(json_data)
    return sort_data
 
 
def get_traces(logistic_code, shipper_code, app_id, app_key, url):
    """查询接口支持按照运单号查询(单个查询)"""
    data1 = {'LogisticCode': logistic_code, 'ShipperCode': shipper_code}
    d1 = json.dumps(data1, sort_keys=True)
    data_sign = encrypt(d1, app_key)
 
    post_data = {
        'RequestData': d1,
        'EBusinessID': app_id,
        'RequestType': '1002',          # 即时查询接口编码
        'DataType': '2',
        'DataSign': data_sign.decode()
    }
    json_data = send_post(url, post_data)
    sort_data = json.loads(json_data)
    return sort_data
 
 
def recognise(express_code):
    express_code = express_code.replace('/test ','')
    """输出数据"""
    url = 'http://api.kdniao.com/Ebusiness/EbusinessOrderHandle.aspx'
    data = get_company(express_code, APP_id, APP_key, url)
    print(data)
    if not data['Shippers']:
        print("未查到该快递信息,请检查快递单号是否有误！")
    else:
        trace_data = get_traces(express_code, data['Shippers'][0]['ShipperCode'], APP_id, APP_key, url)
        print(trace_data)
        if trace_data['Success'] == "false" or not trace_data['Traces']:
            print("未查询到该快递物流轨迹！")
        else:
            str_state = "无轨迹"
            if trace_data['State'] == '1':
                str_state = '已揽收'
            if trace_data['State'] == '2':
                str_state = "在途中"
            if trace_data['State'] == '3':
                str_state = "已签收"
            print("目前状态： "+str_state)
            trace_data = trace_data['Traces']
 
            for item in trace_data:
                print(str(trace_data.index(item))+":", item['AcceptTime'], item['AcceptStation'])
 
            print("\n")
    return
 

if __name__ == '__main__': 
    recognise('2423553456456')
