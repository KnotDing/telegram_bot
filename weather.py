import json
import urllib.request
import time
from random import randint


api_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
units = 'metric'  # kelvin, metric, imperial
lang = 'zh'

def get_wx():
    if api_key == "":
        return False
    try:
        url = 'http://api.openweathermap.org/data/2.5/weather?q=' + location + '&units=' + units + '&lang=' + lang + '&appid=' + api_key + "&v=" + str(randint(0, 100))
        req = urllib.request.Request(url)
        r = urllib.request.urlopen(req).read()
        wx = json.loads(r.decode('utf-8'))
        # wx = json.load(urllib.request.Request().decode('utf-8')
    except:
        return False
    try:
        weather_data = {
            'temperature': str(int(round(wx['main']['temp']))),
            'condition': str(wx['weather'][0]['description']),
            'city': wx['name'],
        }
    except KeyError:
        return False
    return weather_data


def get_wx_for():
    url = 'http://api.openweathermap.org/data/2.5/forecast?q=' + location + '&units=' + units + '&lang=' + lang + '&appid=' + api_key + "&v=" + str(randint(0, 100))
    req = urllib.request.Request(url)
    r = urllib.request.urlopen(req).read()
    wx = json.loads(r.decode('utf-8'))
    return wx

def weath(locate=''):
    global location
    if locate=='/weather':
        location = 'beijing'
    else:
        location = locate.replace('/weather ','')
    weather_data_now = get_wx()
    if weather_data_now is False:
        weather_bot = '(#‵′)靠,查个鬼的天气啊，网不好！'
    else:
        temp = int(weather_data_now['temperature'])
        weather_bot =  weather_data_now['condition'] + ' ' + str(temp) + '°C\n'
        try:
            weather_data_forecast = get_wx_for()
            t = 0
            for i in weather_data_forecast['list']:
                timeArray = time.localtime(int(i['dt']))
                time_for = time.strftime("%m-%d %H:%M", timeArray)
                hour = time.strftime("%H", timeArray)
                if hour == '02':
                    t = t + 1
                    weather_bot += '------------------------------------\n'
                if t == 3:
                    break
                temp = int(round(i['main']['temp']))
                des = str(i['weather'][0]['description']).replace('，', '转')
                slen = len(des)
                while slen < 5:
                    des += '　'
                    slen += 1
                weather_bot += time_for+' ︳ '+des+' ︳'+str(temp) + '°C\n'
        except:
            weath ='(#‵′)靠,查个鬼的天气啊，网不好！'
        weather_bot += 'location:' + weather_data_now['city'] + '\n'
        weather_bot += 'Weather data comes from openweather.'
    return weather_bot

if __name__ == '__main__':
    data = weath()
    print(data)