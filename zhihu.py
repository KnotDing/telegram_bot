import requests
import re
from bs4 import BeautifulSoup


def zhihudaily():
    url = ''
    home_url = 'http://daily.zhihu.com'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
    content = requests.get(home_url,headers = headers)
    all_href = BeautifulSoup(content.text,'lxml').find_all('a',class_ = 'link-button')
    for href in all_href:
        url += '*' + "".join(re.findall(".*<span class=\"title\">(.*)</span>.*", str(href))) + '*\n' + home_url + href['href'] + '\n' 
    return url

if __name__ == '__main__':
    url = zhihudaily()
    print(url)