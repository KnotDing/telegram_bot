import json,requests

def searchPackage(packageData=''):
    if packageData=='/kuaidi':
        pac = '本指令可以根据快递单号进行物流信息查询,可选择输入手机号后四位作为验证'
    #输入运单号码，注意，只有正在途中的快递才可以查到！
    else:
        kuaidi_data = packageData.replace('/kuaidi ','').split(' ')
        packageNum = kuaidi_data[0]
        url1 = 'http://www.kuaidi100.com/autonumber/autoComNum?resultv2=1&text=' + packageNum
        #用url1查询运单号对应的快递公司，如中通，返回：zhongtong。
        companyName = json.loads(requests.get(url1).text)['auto'][0]['comCode']
        #在用url2查询和运单号、快递公司来查询快递详情，结果是一个json文件，用dict保存在resultdict中。
        if len(kuaidi_data)==1:
            url2 = 'http://www.kuaidi100.com/query?type=' + companyName + '&postid=' + packageNum + '&temp=0.21715450266982828'
        else:
            phone = kuaidi_data[1]
            url2 = 'http://www.kuaidi100.com/query?type=' + companyName + '&postid=' + packageNum + '&temp=0.21715450266982828&phone=' + phone
        pac = '单号：' + packageNum + '\n'
        pac += '物流公司：' + companyName + '\n'
        pac += '时间↓                             地点和跟踪进度↓\n'
        for item in json.loads(requests.get(url2).text)['data']:
            pac += item['time'] + ',' + item['context'] + '\n'
    return pac

if __name__ == '__main__':
    data = searchPackage()
    print(data)
