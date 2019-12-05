#                    _ooOoo_
#                   o8888888o
#                   88" . "88
#                   (| -_- |)
#                   O\  =  /O
#                ____/`---'\____
#              .'  \\|     |//  `.
#             /  \\|||  :  |||//  \
#            /  _||||| -:- |||||-  \
#            |   | \\\  -  /// |   |
#            | \_|  ''\---/''  |   |
#            \  .-\__  `-`  ___/-. /
#          ___`. .'  /--.--\  `. . __
#       ."" '<  `.___\_<|>_/___.'  >'"".
#      | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#      \  \ `-.   \_ __\ /__ _/   .-` /  /
# ======`-.____`-.___\_____/___.-`____.-'======
#                    `=---='
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#             佛祖保佑       永无BUG

import requests
import execjs
import re
import os

#os.environ["EXECJS_RUNTIME"] = "PhantomJS"
node = execjs.get()
print(execjs.get().name)
file = './encrypt.js'
ctx = node.compile(open(file,'r',encoding='utf-8').read())

url = 'http://ac.scmor.com/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
}
response = requests.get(url=url, headers=headers)
html = response.content.decode(response.apparent_encoding)
#print(html)
pat_1 = re.compile(r'autourl.*?"(.*?)"')
ls = pat_1.findall(html)
print('len:',len(ls))
for item in ls:
    #print(item)
    href = ctx.call('strdecode',item)
    print(href)
