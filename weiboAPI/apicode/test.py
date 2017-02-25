# _*_ coding: utf-8 _*_

import os
import sys
import weibo
import webbrowser
import json

APP_KEY = '461749408'
MY_APP_SECRET = 'b7e2e172867720ff7b5b3e3f5e152de8'
REDIRECT_URL = 'http://unarimoe.github.io'
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

results = client.statuses__public_timeline()['statuses']

print "************the results is : "
    
    
    ###get_statuses = get_results.__getattr__('statuses')
    
    #statuses = client.statuses__friends_timeline()['statuses'] #获取当前登录用户以及所关注用户（已授权）的微博</span>
    
    length = len(statuses)
        print length
            #输出了部分信息
            for i in range(0,length):
                print '昵称：'+statuses[i]['user']['screen_name']+' 来自：'+statuses[i]['user']['location']
                    print '时间：'+statuses[i]['created_at']+' 位置：'+statuses[i][geo]
                    print '来源：'+statuses[i]['source']
                    print '微博：'+statuses[i]['text']
                    print '转自：'+statuses[i]['retweeted_status']
                    print '图片：'+statuses[i]['thumbnall_pic']
                    print '转发：'+statuses[i]['reposts_count']+' 评论：'+statuses[i]['comments_count']+' 喜欢：'+statuses[i]['attitudes_count']

for st in get_statuses:
    print st.text
json_obg = json.dumps(get_results)
print type(json_obg)

print "*************OK**********"
