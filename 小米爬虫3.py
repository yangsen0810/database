# author:杨森
# date: 2019/11/18 22:13
# file_name: 小米爬虫3
# coding:utf-8
import requests
import re



def get_detail(urls):
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
    json_text = reponse.json()
    if json_text["data"] is None:
        return None
    info = f'{json_text}'
    # print(info)
    # 获取名字
    phone_name = json_text["data"]["goods_info"][0]["name"]
    # 获取价格
    phone_price = json_text["data"]["goods_info"][0]["price"]
    # 获取详情信息
    # phone_detail = json_text["data"]["goods_info"][0]["product_desc"]
    # print(info)
    # phone_detail = re.compile(r'\'product_desc\':.*?「(.*?)"')
    # detail = phone_detail.search(info,re.M | re.S)
    # if detail is None:
    #     phone_detail = re.compile(r"'product_desc'.*?'(.*?)'")
    #     detail = phone_detail.search(info, re.M | re.S)
    # detail = detail.group(1)

    detail = json_text["data"]['product_info']["product_desc"]
    try :
        img_url = json_text["data"]["goods_info"][0]["gallery_v3"]
    except:
        img_url = json_text["data"]["view_content"]["galleryView"]["galleryView"]
    print(phone_name,phone_price,detail)
    for each in range(1,len(img_url)):
        try:
            img_one = "https:"+img_url[each]["img_url"]
        except:
            img_one = "https:"+img_url[each]
        print(img_one)
        if each > 5:
            break
        response = requests.get(img_one)
        with open(f"./data/{phone_name[0:8]+str(each)}.jpg","wb") as f:
            f.write(response.content)


if __name__ == "__main__":
    url = 'https://m.mi.com/v1/home/category_v2'
    # 表单数据
    data = {}
    data['client_id'] = '180100031051'
    data['webp'] = '1'
    head = {}
    head['Accept'] = 'application/json, text/plain, */*'
    head['Accept-Encoding'] = 'gzip, deflate, br'
    head['Accept-Language'] = 'zh-CN,zh;q=0.9'
    head['Connection'] = 'keep-alive'
    head['Content-Length'] = '41'
    head['Content-Type'] = 'application/x-www-form-urlencoded'
    head[
        'Cookie'] = 'xmuuid=XMGUEST-891DD110-AC4E-11E9-8B73-EB4B85C62959; mstuid=1563778897983_6213; XM_agreement=0; Hm_lvt_c3e3e8b3ea48955284516b186acf0f4e=1574042165,1574075189; Hm_lpvt_c3e3e8b3ea48955284516b186acf0f4e=1574075354; Hm_lvt_183aed755f0fd3efc9912dbf6550ec49=1574075368; hd_log_code=m%23bid%3D3480361.0%26gid%3D2194400042%26pid%3D10000198%26stock%3Dtrue%26mihomeId%3D%26provinceId%3D%26cityId%3D%26districtId%3D%26areaId%3D; log_code=be3508ef26ecd981-8c15ef228ff66160|https%3A%2F%2Fm.mi.com%2Fcategory; pageid=be3508ef26ecd981; msttime=https%3A%2F%2Fm.mi.com%2Fcategory; msttime1=https%3A%2F%2Fm.mi.com%2Fcategory; Hm_lpvt_183aed755f0fd3efc9912dbf6550ec49=1574077540; mstz=||1376909953.199|||; xm_vistor=1563778897983_6213_1574075189475-1574077544628'
    head['Host'] = 'm.mi.com'
    head['Origin'] = 'https://m.mi.com'
    head['Referer'] = 'https://m.mi.com/category'
    head[
        'User-Agent'] = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Mobile Safari/537.36'
    head['X-Requested-With'] = 'XMLHttpRequest'
    response = requests.post(url, data=data, headers=head)
    data = response.json()['data']
    # print(data)
    data = data[:19]
    # print(category_list)
    str1 = f'{data}'
    temp = re.compile("'path': '(.*?)'")
    path = temp.findall(str1)
    print(path)
    for each in path:
        if "https" not in each:
            get_detail(each)
