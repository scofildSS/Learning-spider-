import requests

word = input('你想翻译的内容：')
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
data = {
    'i':word,
    'from':'AUTO',
    'to':'AUTO',
    'smartresult':'dict',
    'client':'fanyideskweb',
    'doctype':'json',
    'version':'2.1',
    'keyfrom':'fanyi.web',
    'action':'FY_BY_REALTlME'
}

res = requests.post(url,data=data)
json = res.json()
print(json['translateResult'][0][0]['tgt'])
