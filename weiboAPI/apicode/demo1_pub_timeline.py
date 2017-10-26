# _*_ coding: utf-8 _*_

import sys
import weibo
import webbrowser
reload(sys)                                              # 使用UTF-8输出
sys.setdefaultencoding('utf-8')

APP_KEY = 'xxx'             # 将引号中的xxx替换为你的APP_KEY，保留引号
MY_APP_SECRET = 'yyy'       # 将引号中的yyy替换为你的APP_SECRET，保留引号
REDIRECT_URL = 'zzz'        # 将引号中的zzz替换为你的回调地址，保留引号

# 请求用户授权的过程
client = weibo.APIClient(APP_KEY, MY_APP_SECRET)            #
authorize_url = client.get_authorize_url(REDIRECT_URL)      #

# 自动打开浏览器，授权后复制地址栏中URL里的code字段
webbrowser.open(authorize_url)                              #

# 将code字段后的值复制输入
code = raw_input("input the code: ").strip()                #

# 获得用户授权
request = client.request_access_token(code, REDIRECT_URL)   #

# 保存返回的access_token,exires_in,uid
access_token = request.access_token                         #
expires_in = request.expires_in                             #
uid = request.uid                                           #

# 设置accsess_token
client.set_access_token(access_token, expires_in)           #

# 调用API
results = client.statuses__public_timeline()['statuses']    #

print "-----------the results is : "                        # 输出信息
length = len(results)                                       # 确定获取的信息条数
for i in range(0, length):
    print '昵称：' + results[i]['user']['screen_name'] + \
        ' 来自：' + results[i]['user']['location']
    print '时间：' + results[i]['created_at']
    print '来源：' + results[i]['source']
    print '微博：' + results[i]['text']
    print '转发：' + str(results[i]['reposts_count']) + \
        ' 评论：' + str(results[i]['comments_count']) + \
        ' 喜欢：'+str(results[i]['attitudes_count'])
    print
print "-----------all--------------"
