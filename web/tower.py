import requests
import datetime
from bs4 import BeautifulSoup
url='https://tower.im/members/d9c74caa00784702afa14b6ea8381467/todos/completed/'
cookies=dict(_tower2_session='614336951d25df843d61dad4d19ccc96')
html=requests.get(url,cookies=cookies).text
#print (html)
soup=BeautifulSoup(html, "lxml")
flag=0
for x in soup.body.find('div',class_='container workspace').find_all('div',class_='day'):
    tasktime=x.find('span',class_='m-d').string
    year=datetime.datetime.now().year
    tasktime=str(year)+'/'+tasktime
    weekday=datetime.datetime.now().weekday()
    monday=(datetime.datetime.now()-datetime.timedelta(weekday)).strftime('%Y/%m/%d')
    t_arr = tasktime.split('/')
    t_arr=[i.zfill(2) for i in t_arr]
    tasktime=t_arr[0]+'/'+t_arr[1]+'/'+t_arr[2]
    if tasktime < monday:
        break
    y=x.stripped_strings
    for z in y:
        if z[-1]=='：':
            print(z,end='')
        else :
            print (z)
