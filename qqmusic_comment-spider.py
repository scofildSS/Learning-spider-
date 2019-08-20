from selenium import  webdriver
from bs4 import BeautifulSoup
import time

#-----------------第一种方法-------------------------------

driver = webdriver.Chrome()

driver.get('https://y.qq.com/n/yqq/song/000xdZuV2LcQ19.html') # 访问页面
time.sleep(2)

button = driver.find_element_by_class_name('js_get_more_hot') # 根据类名找到【点击加载更多】
button.click() # 点击
time.sleep(2) # 等待两秒

comments = driver.find_element_by_class_name('js_hot_list').find_elements_by_class_name('js_cmt_li') #  使用class_name找到评论
print(len(comments)) # 打印获取到的评论个数
for comment in comments: # 遍历列表
    sweet = comment.find_element_by_tag_name('p') # 找到评论
    print ('评论：%s\n ---\n'%sweet.text) # 打印评论

driver.close() # 关闭浏览器

#-----------------第二种方法-------------------------------
driver = webdriver.Chrome()

driver.get('https://y.qq.com/n/yqq/song/000xdZuV2LcQ19.html') # 访问页面
time.sleep(2)

button = driver.find_element_by_class_name('js_get_more_hot') # 根据类名找到【点击加载更多】
button.click() # 点击
time.sleep(2) # 等待两秒

pageSource = driver.page_source # 获取Elements中渲染完成的网页源代码
soup = BeautifulSoup(pageSource,'html.parser')  # 使用bs解析网页
comments = soup.find('ul',class_='js_hot_list').find_all('li',class_='js_cmt_li') # 使用bs提取元素
print(len(comments)) # 打印comments的数量

for comment in comments: # 循环
    sweet = comment.find('p') # 提取评论
    print ('评论：%s\n ---\n'%sweet.text) # 打印评论
driver.close() # 关闭浏览器 
