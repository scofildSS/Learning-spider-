import requests

def login(session, headers):
#模拟登陆
    url_1 = 'https://h5.ele.me/restapi/eus/login/mobile_send_code'
    tel = input('请输入手机号码：')
    data_1 = {
        'captcha_hash':"",
        'captcha_value':"",
        'mobile':tel,
        'scf':"ms"
    }
    token = session.post(url_1, headers=headers, data=data_1).json()['validate_token']
    #请求发送验证码

    url_2 = 'https://h5.ele.me/restapi/eus/login/login_by_mobile'
    code = input('请输入验证码：')
    data_2 = {
    'mobile':tel,
    'scf':"ms",
    'validate_code':code,
    'validate_token':token
    }
    session.post(url_2, headers=headers, data=data_2)
    #向服务器提交登陆信息

def place(headers):
#模拟输入地址
    address_url = 'https://www.ele.me/restapi/bgs/poi/search_poi_nearby?'
    place = input('请输入你的收货地址：')
    # 因为我的geohash使用了深圳的值，所以推荐你测试的时候使用“腾讯大厦”。
    params = {
        'geohash': 'ws105rz9smwm',
        'keyword': place,
        'latitude': '22.54286',
        'limit': '20',
        'longitude': '114.059563',
        'type': 'nearby'
    }
    address_res = requests.get(address_url, params=params, headers=headers)
    # 发起请求
    address_json = address_res.json()
    # 将响应的结果转为列表/字典。

    print('以下，是与' + place + '相关的位置信息：\n')
    n = 0

    for address in address_json:
        # 遍历我们刚爬取的地址列表。
        print(str(n) + '. ' + address['name'] + '：' + address['short_address'] + '\n')
        # 打印序号，地址名，短地址。
        n = n + 1

    address_num = int(input('请输入您选择位置的序号：'))
    # 让用户选择序号。
    final_address = address_json[address_num]
    # 确认地址。

    print(final_address['geohash'])
    print(final_address['latitude'])
    print(final_address['longitude'])
    return final_address

def restaurants(session, headers, final_address):
#请求餐馆列表
    url = 'https://www.ele.me/restapi/shopping/restaurants?'
    params = {
        'extras[]': 'activities',
        'geohash': final_address['geohash'],
        'latitude': final_address['latitude'],
        'limit': '24',
        'longitude': final_address['longitude'],
        'offset': '0',
        'terminal': 'web'
    }
    #将参数封装，其中geohash和经纬度，来自前面获取到的数据。
    res = session.get(url, headers=headers, params=params)
    json_rest = res.json()
    for rest in json_rest:
        print(rest['name'])
    #遍历每个restaurant的名称，rest中包含了单个餐厅的所有信息


session = requests.session()
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
login(session,headers)
final_address = place(headers)
restaurants(session, headers, final_address)
