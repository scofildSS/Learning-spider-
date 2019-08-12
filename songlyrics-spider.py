import requests
# 引用requests模块
url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
# 请求歌曲歌词的url参数的前面部分
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }

for i in range(5):
    params = {
    'ct':'24',
    'qqmusic_ver':'1298',
    'remoteplace':'txt.yqq.lyric',
    'searchid':'99376184556095507',
    'aggr':'0',
    'catZhida':'1',
    'lossless':'0',
    'sem':'1',
    't':'7',
    'p':str(i),
    'n':'5',
    'w':'周杰伦',  #此处可以换成其他歌手
    'g_tk':'5381',
    'loginUin':'0',
    'hostUin':'0',
    'format':'json',
    'inCharset':'utf8',
    'outCharset':'utf-8',
    'notice':'0',
    'platform':'yqq.json',
    'needNewCode':'0'
    }
    # 将参数封装为字典
    res_comments = requests.get(url, headers = headers ,params = params)
    # 调用get方法，下载这个字典
    json_lyrics = res_comments.json()
    list_lyrics = json_lyrics['data']['lyric']['list']
    #找到歌词的位置
    for lyrics in list_lyrics:
        print(lyrics['content'])
        print('-----------------------------------')
        #打印歌词
