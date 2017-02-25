# _*_ coding: utf-8 _*_

import os
import sys
import weibo
import webbrowser
import json
reload(sys)
sys.setdefaultencoding('utf-8')

APP_KEY = '461749408'
MY_APP_SECRET = 'b7e2e172867720ff7b5b3e3f5e152de8'
REDIRECT_URL = 'http://rimoe.ml/2017/02/04/apicallback'
#这个是设置回调地址，必须与那个”高级信息“里的一致

#请求用户授权的过程
client = weibo.APIClient(APP_KEY, MY_APP_SECRET)

authorize_url = client.get_authorize_url(REDIRECT_URL)


#打开浏览器，需手动找到地址栏中URL里的code字段
webbrowser.open(authorize_url)

#将code字段后的值输入控制台中
code = raw_input("input the code: ").strip()

#获得用户授权
request = client.request_access_token(code, REDIRECT_URL)
#request = client.statuses.public_timeline.get()

#保存access_token ,exires_in, uid
access_token = request.access_token
expires_in = request.expires_in
uid = request.uid


#设置accsess_token
client.set_access_token(access_token, expires_in)


#get_results = client.statuses__mentions()
#get_results = client.frientdships__friends__ids()
#get_results = client.statuses__user_timeline()
#get_results = client.statuses__repost_timeline(id = uid)
#get_results = client.search__topics(q = "笨NANA")
all=0
s=""
file = open("result.txt", "w")
while all<=2000:
    results = client.statuses__public_timeline()['statuses']
    
    ###get_statuses = get_results.__getattr__('statuses')
    
    #statuses = client.statuses__friends_timeline()['statuses'] #获取当前登录用户以及所关注用户（已授权）的微博</span>

    length = len(results)
    all+=length
    print length

            #输出了部分信息
    for i in range(0,length):
        s1=u'昵称：'+results[i]['user']['screen_name']+u' 来自：'+results[i]['user']['location']
        s2=u'时间：'+results[i]['created_at']#+u' 位置：'+results[i][geo][province_name]+results[i][geo][city_name]+results[i][geo][address]
        s3=u'来源：'+results[i]['source']
        s4=u'微博：'+results[i]['text']
    #print u'转自：'+results[i]['retweeted_status']
    #print u'图片：'+results[i]['thumbnall_pic']
        s5='report/review/like：'+str(results[i]['reposts_count'])+' '+str(results[i]['comments_count'])+' '+str(results[i]['attitudes_count'])
        s='********'+'\n'+str(all)+'.'+str(i)+'\n'+s1+'\n'+s2+'\n'+s3+'\n'+s4+'\n'+s5
        file.write(s)
file.close()
#print "$$$$$$$"
#for st in results:
#    print st.text
#print "$$$$$$$"
#json_obg = json.dumps(results)
#print type(json_obg)

print "*************OK**********"
