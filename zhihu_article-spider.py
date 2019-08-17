import requests
import csv

csv_file=open('articles.csv','w',newline='',encoding='utf-8')
#调用open()函数打开csv文件
writer = csv.writer(csv_file)
#创建一个writer对象。
list2=['标题','链接','摘要']
writer.writerow(list2)
#在csv文件里写入一行文字 “标题”和“链接”和"摘要"。

headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
url='https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles?'
offset=0

while True:
    params={
        'include':'data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics',
        'offset':str(offset),
        'limit':'20',
        'sort_by':'voteups',
        }

    res=requests.get(url,headers=headers,params=params)
    #发送请求
    articles=res.json()
    print(articles)
    data=articles['data']
    #定位数据
    for i in data:
        list1=[i['title'],i['url'],i['excerpt']]
        #把目标数据封装成一个列表
        writer.writerow(list1)
        #把列表list1的内容写入
    offset=offset+20

    if offset > 40:
        break
csv_file.close()
#写入完成后，关闭文件
print('okay')
