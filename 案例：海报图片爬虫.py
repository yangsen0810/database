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
import datetime
import json
from lxml import etree
import time
import random


headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)',
}

url = 'http://pic.haibao.com/hotimage/'
html = requests.get(url,headers=headers).text
html = etree.HTML(html)
ls = html.xpath('//div[@class="pagelibox"]//img/@data-original')
print('len:',len(ls))
# for link in ls:
#     image = requests.get(link,headers=headers).content
#     image_name = link.split('/')[-1]
#     image_name = './images/'+image_name
#     print(image_name)
#     with open(image_name,'wb') as file:
#         file.write(image)

# 模拟ajax请求
ajax_url = 'http://pic.haibao.com/ajax/image:getHotImageList.json?stamp='
skip = len(ls)
# Mon Oct 28 2019 16:11:58 GMT 0800 (中国标准时间)
while True:
    GTM_FORMAT = '%a %b %d %Y %H:%M:%S GMT 0800'
    stamp = datetime.datetime.utcnow().strftime(GTM_FORMAT)
    stamp = stamp + ' (中国标准时间)'
    print('stamp:',stamp)
    new_url = ajax_url +stamp
    data = {
        'skip':skip,
    }

    print('new_url:',new_url)
    html = requests.post(new_url,data=data,headers=headers).text
    data = json.loads(html)
    skip = data['result']['skip']
    html = data['result']['html']
    print('skip:',skip)
    if html !=None:
        html = etree.HTML(html)
        ls = html.xpath('//img[@class="lazys"]/@data-original')
        print('len:',len(ls))
        for link in ls:
            image = requests.get(link,headers=headers).content
            image_name = link.split('/')[-1]
            image_name = './images/'+image_name
            print(image_name)
            with open(image_name,'wb') as file:
                file.write(image)
            time.sleep(random.random()*2)
    else:
        break;








