import requests
url1='https://tower.im/users/sign_in'
re1=requests.get(url1) 
coo=re1.headers['Set-Cookie'].split(';')[0]
coo_a=coo.split('=')[0]
coo_b=coo.split('=')[1]
cookie1={coo_a:coo_b}
print ('cookie1:')
print (cookie1)
url2='https://tower.im/users/sign_in'
re2=requests.post(url2,cookies=cookie1)
cookie2=re2.headers
print ('cookie2:')
print (cookie2)
