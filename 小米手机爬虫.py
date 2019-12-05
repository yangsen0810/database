# author:杨森
# date: 2019/11/18 17:41
# file_name: 小米手机爬虫
import requests
from selenium import webdriver
import time
import re
from lxml import etree
from selenium.webdriver.chrome.options import Options
import pymysql

if __name__ == "__main__":
    url = "https://m.mi.com"
    mobile_emulation = {'deviceName': 'iPhone 6'}
    options = webdriver.ChromeOptions()
    # 数据库连接
    conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456", database="myhome")
    # 设置为无界面浏览器
    options.add_argument('--headless')
    #设置为手机版
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)
    time.sleep(3)
    driver.find_element_by_xpath("//div[@class='fill-height box-flex align-center']//a[@class='flex']").click()
    time.sleep(3)
    html = driver.page_source
    result = etree.HTML(html)
    #提取手机信息 这个会提取很多注意
    # all_info = result.xpath("//div[@index='2']/div[@class='box']//div[@class='product']")
    # pat_compile = re.compile("pid=(.*?)&")
    # for each in range(11):
    #     time.sleep(3)
    #     # 获取手机名称
    #     phone_name = all_info[each].xpath("./a//div[@class='name']/text()")[0]
    #     pcode = all_info[each].xpath("./a/@data-log_code")[0]
    #     pid = pat_compile.search(pcode,re.M | re.S).group(1)
    #     # 请求详情页
    #     href = "https://m.mi.com/commodity/detail/"+pid
    #     driver.get(href)
    #     time.sleep(3)
    #     detailhtml = driver.page_source
    #     new_html = etree.HTML(detailhtml)
    #     # 获取手机描述
    #     content = new_html.xpath("//div[@class='goods-brief fz-xs']/text()")[0]
    #     # 获取手机的价钱
    #     price = new_html.xpath("//div[@class='price cur-price']/text()")[0]
    #     # 提取评论的前5条内容
    #     comments = new_html.xpath("//div[@class='comment-content']")
    #     comment_list = []
    #     for each in range(len(comments)):
    #         comment_list.append(comments[each].xpath("./div[@class='text fz-xs']/text()")[0])
    #     # 爬取规格信息
    #     all_drive = new_html.xpath("//div[@class='classic-param-item-name fz-xs']/text()")
    #     # 爬取规格对应的信息
    #     all_drivce_info = new_html.xpath("//div[@class='classic-param-item-value fz-xxs']/text()")
    #     drivce_info = dict(zip(all_drive,all_drivce_info))
    #     img_compile = re.compile('<img data-v-ccdb1440="".*?src="(.*?)"')
    #     all_img = img_compile.findall(detailhtml, re.M | re.S)
    #     # 下载图片
    #     for each in range(1,6):
    #         img_url = "http:"+str(all_img[each])
    #         img_response = requests.get(img_url)
    #         with open(f"./data/{phone_name+str(each)}.jpg","wb") as f:
    #             f.write(img_response.content)
    #     # 定义产品类型
    #     types = "手机"
    #     # 将comments 进行存储
    #     comments = "".join(comment_list)
    #     # 将规格信息存储dict
    #     drivce_infos = ""
    #     for key,val in drivce_info.items():
    #         drivce_infos += key+":"+val+","
    #     print(comments)
    #     print(drivce_infos)
    #     with conn.cursor(pymysql.cursors.DictCursor) as curs:
    #         sql = "insert into phone values (%s,%s,%s,%s,%s,%s)"
    #         try:
    #             curs.execute(sql, args=(phone_name,content, price, comments,drivce_infos,types))
    #             conn.commit()
    #         except:
    #             curs.execute(sql, args=(phone_name, content, price, "不错", drivce_infos,types))
    #             conn.commit()
    #             continue
    # conn.close()

    # 进行爬取电视机
    all_info = result.xpath("//div[@index='4']/div[@class='box']//div[@class='product']")
    pat_compile = re.compile("pid=(.*?)&")
    for each in range(6):
        time.sleep(3)
        # 获取家电名称
        tv_name = all_info[each].xpath("./a//div[@class='name']/text()")[0]
        pcode = all_info[each].xpath("./a/@data-log_code")[0]
        pid = pat_compile.search(pcode, re.M | re.S).group(1)
        href = "https://m.mi.com/commodity/detail/" + pid
        driver.get(href)
        time.sleep(3)
        detailhtml = driver.page_source
        print(detailhtml)
        new_html = etree.HTML(detailhtml)
        # 获取电脑描述
        content = new_html.xpath("//div[@class='goods-brief fz-xs']/text()")[0]
        # 获取电脑的价钱
        price = new_html.xpath("//div[@class='price cur-price']/text()")[0]
        # 提取评论的前5条内容
        comments = new_html.xpath("//div[@class='comment-content']")
        comment_list = []
        for each in range(len(comments)):
            comment_list.append(comments[each].xpath("./div[@class='text fz-xs']/text()")[0])
        # 爬取规格信息
        all_drive = new_html.xpath("//div[@class='classic-param-item-name fz-xs']/text()")
        # 爬取规格对应的信息
        all_drivce_info = new_html.xpath("//div[@class='classic-param-item-value fz-xxs']/text()")
        drivce_info = dict(zip(all_drive, all_drivce_info))
        img_compile = re.compile('<img data-v-ccdb1440="".*?src="(.*?)"')
        all_img = img_compile.findall(detailhtml, re.M | re.S)
        # 下载图片
        for each in range(1, 6):
            img_url = "http:" + str(all_img[each])
            img_response = requests.get(img_url)
            with open(f"./data/{tv_name + str(each)}.jpg", "wb") as f:
                f.write(img_response.content)
        # 定义产品类型
        types = "家电"
        print(tv_name,content,price,comment_list,drivce_info)







