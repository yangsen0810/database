# author:杨森
# date: 2019/11/18 21:55
# file_name: 小米手机爬虫
# author 黄强
# date 2019/11/18 17:54
# file_name xiaomi

import requests
from lxml import etree

def sun1():
    url="https://m.mi.com/v1/home/category_v2"
    headers={
        # 'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)',

        'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
        'Referer': 'https://m.mi.com/category',

    }
    data={
        'client_id': 180100031051,
        'webp': 1
    }
    reponse=requests.post(url,data=data,verify=True,headers=headers)
    text=reponse.json()
    # print(text)
    data=text['data']
    for i in data[:19]:
        name=i["category_name"]
        a=i["category_list"]
        print(len(a))
        for i in a:
            if i["view_type"]=='category_group':
                b=i["body"]["items"]
                for j in b:
                    url=j["action"]["path"]
                    if 'http' in url:
                        url=url.split("/")[-1]
                    # print(url)
                    sun2(url)
        print(f'{name}商品爬取完')
# s=0
def sun2(urls):
    # print(urls)
    url = "https://m.mi.com/v1/miproduct/view"
    headers = {
        'Referer': f'https://m.mi.com/commodity/detail/{str(urls)}',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    }
    data = {
        'client_id': 180100031051,
        'webp': 1,
        'commodity_id': urls,
        'pid': urls
    }
    reponse = requests.post(url, data=data, verify=True, headers=headers)
    json_text=reponse.json()
    a_pz=json_text["data"]["buy_option"]
    for i in a_pz:
        print(i['name'])
        list=i["list"]
        for i in list:
            name=i["name"]
            money=i["price"]
            print(name,money)




    # global s
    # s+=1
    # print(s)
if __name__ == '__main__':
    sun1()





# print(len(data))

