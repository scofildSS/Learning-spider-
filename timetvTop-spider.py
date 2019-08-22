from gevent import monkey
monkey.patch_all()
#monkey.patch_all()能把程序变成协作式运行，就是可以帮助程序实现异步。
import gevent,requests,bs4,csv
from gevent.queue import Queue

work = Queue()
#创建队列对象
url_1 = 'http://www.mtime.com/top/tv/top100/'
work.put_nowait(url_1)
#第一页网址和后来的网址规则不一样
url_2 = 'http://www.mtime.com/top/tv/top100/index-{page}.html'
for x in range(1,11):
    real_url = url_2.format(page=x)
    work.put_nowait(real_url)
#用put_nowait()函数可以把网址都放进队列里

def crawler():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    while not work.empty():
    # 当队列不是空的时候，就执行下面的程序。
        url = work.get_nowait()
        # 用get_nowait()函数可以把队列里的网址都取出。
        res = requests.get(url,headers=headers)
        bs_res = bs4.BeautifulSoup(res.text,'html.parser')
        datas = bs_res.find_all('div',class_="mov_con")
        for data in datas:
            TV_title = data.find('a').text
            data = data.find_all('p')
            TV_data =''
            for i in data:
                TV_data =TV_data + ''+ i.text
            writer.writerow([TV_title,TV_data])
            print([TV_title,TV_data])

csv_file = open('timetop.csv','w',newline='',encoding='utf-8')
writer = csv.writer(csv_file)

task_list = []
for x in range(3):
# 相当于创建了3个爬虫
    task = gevent.spawn(crawler)
    #用gevent.spawn()函数创建执行crawler()函数的任务。
    task_list.append(task)
    #往任务列表添加任务。
gevent.joinall(task_list)
#用gevent.joinall方法，执行任务列表里的所有任务
