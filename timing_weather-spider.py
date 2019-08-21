import requests
import smtplib
import schedule
import time
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.header import Header

account = input('请输入你的邮箱：')
password = input('请输入你的密码：')
receiver = input('请输入收件人的邮箱：')

def weather_spider():
#爬取天气信息
    headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    url='http://www.weather.com.cn/weather/101280601.shtml'
    res=requests.get(url,headers=headers)
    res.encoding='utf-8'
    soup=BeautifulSoup(res.text,'html.parser')
    tem1= soup.find(class_='tem')
    weather1= soup.find(class_='wea')
    tem=tem1.text
    weather=weather1.text
    return tem,weather

def send_email(tem,weather):
#把天气信息发送到邮件
    global account,password,receiver
    mailhost='smtp.qq.com'
    #qq邮箱的服务器地址
    qqmail = smtplib.SMTP()
    qqmail.connect(mailhost,25)
    #连接服务器
    qqmail.login(account,password)
    #登录邮箱
    content= tem+weather
    message = MIMEText(content, 'plain', 'utf-8')
    #邮件内容
    subject = '今日天气预报'
    message['Subject'] = Header(subject, 'utf-8')
    #邮件主题
    try:
        qqmail.sendmail(account, receiver, message.as_string())
        #发送邮件
        print ('邮件发送成功')
    except:
        print ('邮件发送失败')
    qqmail.quit()
    #退出邮箱

def job():
#定时执行的任务
    print('开始一次任务')
    tem,weather = weather_spider()
    send_email(tem,weather)
    print('任务完成')

schedule.every().day.at("07:30").do(job)
#设置每天07：30执行任务
while True:
    schedule.run_pending()
    #执行
    time.sleep(1)
