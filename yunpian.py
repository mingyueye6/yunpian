# coding: utf-8
# 云片网短信平台
import requests

APIKEY = ''

def send_message(code, phone):
    # code 验证码，phone 手机号
    url = 'https://sms.yunpian.com/v2/sms/single_send.json'
    text = '您的验证码是{}'.format(code)
    headers = {
        'Accept': 'application/json;charset=utf-8;',
        'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8;'
    }
    data = {
        'apikey': APIKEY,
        'mobile': phone,
        'text': text
    }
    res = requests.post(url, data=data, headers=headers)
    res.encoding = 'utf-8'
    content = res.json()
    print(content)
    # {
    #     "code": 0,
    #     "msg": "发送成功",
    #     "count": 1,
    #     "fee": 0.05,
    #     "unit": "RMB",
    #     "mobile": "17303802082",
    #     "sid": 47432515906
    # }


if __name__ == '__main__':
    send_message('123456', '')

