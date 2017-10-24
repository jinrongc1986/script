import urllib
from urllib import request, parse
import json
import ssl
import requests
import base64


def ali_yzm(imgurl):
    host = 'https://ali-checkcode2.showapi.com'
    path = '/checkcode'
    appcode = 'f9950167094d4f6caf5d16d927521280'
    appcode = '97a9afe050ac4126aea926d2c432a2eb'
    bodys = {}
    url = host + path
    url = 'http://route.showapi.com/184-5'

    bodys['convert_to_jpg'] = '0'
    bodys['img_base64'] = imgurl
    bodys['typeId'] = '30'
    post_data = parse.urlencode(bodys).encode('utf-8')
    requesturl = request.Request(url, post_data)
    requesturl.add_header('Authorization', 'APPCODE ' + appcode)
    requesturl.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    response = urllib.request.urlopen(requesturl, context=ctx)
    content = response.read()
    try:
        return json.loads(content.decode("utf-8"))["showapi_res_body"]["Result"]
    except Exception as e:
        print(e)
        return ""

def showapi_yzm(imgurl):
    showapi_appid = "48565"  # 替换此值
    showapi_sign = "97a9afe050ac4126aea926d2c432a2eb"  # 替换此值
    url = "http://route.showapi.com/184-5"
    send_data = parse.urlencode([
        ('showapi_appid', showapi_appid)
        , ('showapi_sign', showapi_sign)
        , ('img_base64', imgurl)
        , ('typeId', "30")
        , ('convert_to_jpg', "0")

    ])
    req = request.Request(url)
    try:
        response = request.urlopen(req, data=send_data.encode('utf-8'), timeout=10)  # 10秒超时反馈
    except Exception as e:
        print(e)
    try:
        result = response.read().decode('utf-8')
        result_json = json.loads(result)
        return result_json["showapi_res_body"]["Result"]
    except Exception as e:
        print(e)
        return ""


if __name__ == '__main__':
    # imgurl = "data:image/jpeg;base64, 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"
    # url=imgurl.split(',')[1]
    # print (main(url))
    imgname = 'xmxqb_3018.jpg'
    with open(imgname, 'rb') as f:
        data = base64.b64encode(f.read()).decode("utf-8")
    imgurl="data:image/jpeg;base64, "+data
    print (imgurl)
    print (ali_yzm(imgurl))
    print(showapi_yzm(imgurl))
