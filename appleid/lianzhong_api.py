# coding: utf-8
import requests

def main(file_name,api_username="jinrongc", api_password="FxData!Cds@2016_", api_post_url="http://v1-http-api.jsdama.com/api.php?mod=php&act=upload"):
    '''
            main() 参数介绍
            api_username    （API账号）             --必须提供
            api_password    （API账号密码）         --必须提供
            file_name       （需要打码的图片路径）   --必须提供
            api_post_url    （API接口地址）         --必须提供
            yzm_min         （验证码最小值）        --可空提供
            yzm_max         （验证码最大值）        --可空提供
            yzm_type        （验证码类型）          --可空提供
            tools_token     （工具或软件token）     --可空提供
    '''
    # api_username =
    # api_password = 
    # file_name = 'c:/temp/lianzhong_vcode.png'
    # api_post_url = "http://v1-http-api.jsdama.com/api.php?mod=php&act=upload"
    # yzm_min = '1'
    # yzm_max = '8'
    # yzm_type = '1303'
    # tools_token = api_username

    # proxies = {'http': 'http://127.0.0.1:8888'}
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
        # 'Content-Type': 'multipart/form-data; boundary=---------------------------227973204131376',
        'Connection': 'keep-alive',
        'Host': 'v1-http-api.jsdama.com',
        'Upgrade-Insecure-Requests': '1'
    }

    files = {
        'upload': (file_name, open(file_name, 'rb'), 'image/png')
    }

    data = {
        'user_name': api_username,
        'user_pw': api_password
    }
    s = requests.session()
    # r = s.post(api_post_url, headers=headers, data=data, files=files, verify=False, proxies=proxies)
    r = s.post(api_post_url, headers=headers, data=data, files=files, verify=False)
    #print(r.text)  #{"data":{"val":"FAA4","id":8631454506},"result":true}
    return(r.text)

def report(yzm_id,api_username="jinrongc", api_password="FxData!Cds@2016_", api_post_url="http://v1-http-api.jsdama.com/api.php?mod=php&act=error"):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
        # 'Content-Type': 'multipart/form-data; boundary=---------------------------227973204131376',
        'Connection': 'keep-alive',
        'Host': 'v1-http-api.jsdama.com',
        'Upgrade-Insecure-Requests': '1'
    }
    data = {
        'user_name': api_username,
        'user_pw': api_password,
        'yzm_id': yzm_id
    }
    s = requests.session()
    r = s.post(api_post_url, headers=headers, data=data,verify=False)
    print (r.text)
    return(r.text)


def download_vcode():
    try:
        url = 'https://kyfw.12306.cn/otn/passcodeNew/getPassCodeNew?module=login&rand=sjrand&0.8126458147235742'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'}
        s = requests.session()
        resp = s.get(url, headers=headers, verify=False)
        file_name = 'c:/temp/lianzhong_vcode.png'
        with open(file_name, 'wb') as f:
            f.write(resp.content)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # download_vcode()
    main(file_name = 'test.jpg',
		api_username ="jinrongc",
        api_password = "FxData!Cds@2016_",
        api_post_url = "http://v1-http-api.jsdama.com/api.php?mod=php&act=upload")

    '''
        main() 参数介绍
        api_username    （API账号）             --必须提供
        api_password    （API账号密码）         --必须提供
        file_name       （需要打码的图片路径）   --必须提供
        api_post_url    （API接口地址）         --必须提供
        yzm_min         （验证码最小值）        --可空提供
        yzm_max         （验证码最大值）        --可空提供
        yzm_type        （验证码类型）          --可空提供
        tools_token     （工具或软件token）     --可空提供
    '''
