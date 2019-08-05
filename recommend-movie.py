import requests
from bs4 import BeautifulSoup
import random

def release_movie_spider():
#爬取最近上映的电影
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    #请求用户代理
    res = requests.get('https://movie.douban.com/', headers =headers)
    html = res.content.decode('utf-8')
    #获取数据
    soup = BeautifulSoup(html, 'html.parser')
    #解析数据
    list_movie_content = soup.find_all('li', attrs={'data-enough':"true"})[:5]
    #找到含有电影信息的<li>标签
    top5_release_movie = []
    for movie_content in list_movie_content:
        name = movie_content['data-title']
        #电影名
        rating = movie_content['data-rate']
        #评分
        director = movie_content['data-director']
        #导演
        actors = movie_content['data-actors']
        #演员
        top5_release_movie.append([name, rating, director, actors])
        #把信息添加到列表

    release_movie = random.choice(top5_release_movie)
    #从列表中随机选择
    print('最近上映电影：' + str(release_movie))

def hot_movie_spider():
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    params = {
        'type':'movie',
        'tag':'热门',
        'page_limit':'50',
        'page_start':'0'
    }
    # 将参数封装为字典
    res1 = requests.get('https://movie.douban.com/j/search_subjects', headers =headers, params = params)
    json = res1.json()
    #将json数据转为字典或列表
    all_hot_movie = []
    for hot_movie_content in json['subjects']:
        name = hot_movie_content['title']
        #片名
        rate = hot_movie_content['rate']
        #评分
        all_hot_movie.append([name, rate])

    hot_movie = random.choice(all_hot_movie)
    # 从列表中随机选择
    print('最近热门电影：' + str(hot_movie))

way = input('推荐最近上映电影请输入1；推荐最近热门电影请输入2！请输入：')
if way == '1':
    release_movie_spider()
    #输入1推荐最近上映电影

elif way == '2':
    hot_movie_spider()
    #输入2推荐最近热门电影

else:
    print('抱歉，没有这个选项！')
