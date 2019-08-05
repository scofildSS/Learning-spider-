import requests
from bs4 import BeautifulSoup
from urllib.request import quote

url = 'http://s.ygdy8.com/plus/so.php?typeid=1&keyword='
#基础url
movie_name = input('请输入要查找的电影名：')
#输入电影名
moviename_gbk = movie_name.encode('gbk')
#电影名转gbk格式
movie_url = url + quote(moviename_gbk)
# quote()函数，可以帮我们把内容转为标准的url格式，作为网址的一部分打开

res = requests.get(movie_url)
html = res.content.decode('gbk','ignore')
#获取数据
soup = BeautifulSoup(html, 'html.parser')
#解析数据
content = soup.find('div', class_="co_content8")
#查找<div class="co_content8">标签
content_ul = content.find('ul')
#查找<ul>标签
item_list = content_ul.find_all('a')
#查找包含每一项信息的标签<a>
movie_link = []

for item in item_list:
    item_name = item.text
    #获取每一项名字
    item_url = 'https://www.ygdy8.com' + item['href']
    #组成新的url，进入获取链接
    res1 = requests.get(item_url)
    html1 = res1.content.decode('gbk', 'ignore')
    soup1 = BeautifulSoup(html1, 'html.parser')
    movie_content = soup1.find('div', id="Zoom")
    #查找<div id="Zoom">标签
    movie_content_a = movie_content.find('a')
    #查找含有链接的标签<a>
    try:
        link = movie_content_a['href']
    except:
        link = 'null'
    #防止有一些是没有找到链接的
    movie_link.append([item_name,link])
    #添加进总列表

print(movie_link)
#打印
