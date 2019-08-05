import requests
from bs4 import BeautifulSoup
import csv

movie_top250 = [['序号', '电影名', '评分', '推荐语', '链接']]
#创建一个列表
for i in range(0, 250, 25):
    #发现每页url的规律
    url = 'https://movie.douban.com/top250?start=' + str(i) + '&filter='
    res = requests.get(url)
    html = res.content.decode('utf-8')
    #获取数据
    soup = BeautifulSoup(html, 'html.parser')
    #解析数据
    list_item = soup.find_all('div',class_="item")
    #查找包含电影信息的<div>标签
    movie_all = []
    #创建一个空列表
    for item in list_item:
        sequence = item.find('em')
        #获取序号
        name = item.find('span', class_="title")
        #获取电影名
        score = item.find('span', class_="rating_num")
        #获取评分
        recommend = item.find('span', class_="inq")
        if recommend ==None:
        #防止推荐语为None
            recommend_a = 'null'
        else:
            recommend_a = recommend.text
        #获取推荐语
        tag = item.find('div', class_="hd")
        tag_a = tag.find('a')
        #获取包含链接的<a>标签
        movie_all.append([sequence.text, name.text, score.text, recommend_a, tag_a['href']])

    movie_top250 += movie_all
    #把每页电影信息添加到总列表中

print(movie_top250)
#打印

with open('doubanMovie_top250.csv', 'w', encoding='UTF-8', newline='') as f:
#把列表写入表格中
    writer = csv.writer(f)
    for each in movie_top250:
        writer.writerow(each)

print('write over !')
