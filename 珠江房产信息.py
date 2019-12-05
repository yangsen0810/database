# author:杨森
# date: 2019/11/12 18:52
# file_name: 爬取中储粮
from selenium import webdriver
import time
import requests

def get_url(url):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url=url)
    time.sleep(7)
    # 点击房产信息页面
    info = driver.find_elements_by_xpath("//div[@class='data-grid']//tr")
    for each in info[1:]:
        each.find_elements_by_xpath(".//td")[1].click()
        print(each.find_elements_by_xpath(".//td")[1].text)
        name = each.find_elements_by_xpath(".//td")[1].text
        time.sleep(5)
        # 获取img标签的连接
        imgurl = driver.find_element_by_xpath("//div[@class='layui-layer-content']//img").get_attribute("src")
        print(imgurl)
        # 调用下载图片
        get_img(imgurl,name)
        driver.find_element_by_xpath("//a[@class='layui-layer-ico layui-layer-close layui-layer-close1']").click()
    # 进行翻页操作
    while True:
        driver.find_element_by_xpath("//div[@id='pages']//a[@class='next']").click()
        time.sleep(7)
        info = driver.find_elements_by_xpath("//div[@class='data-grid']//tr")
        for each in info[1:]:
            each.find_elements_by_xpath(".//td")[1].click()
            print(each.find_elements_by_xpath(".//td")[1].text)
            name = each.find_elements_by_xpath(".//td")[1].text
            time.sleep(5)
            # 获取img标签的连接
            imgurl = driver.find_element_by_xpath("//div[@class='layui-layer-content']//img").get_attribute("src")
            print(imgurl)
            # 调用下载图片
            get_img(imgurl, name)
            driver.find_element_by_xpath("//a[@class='layui-layer-ico layui-layer-close layui-layer-close1']").click()




def get_img(url,name):
    response = requests.get(url)
    with open(f"./images/{name}.jpg","wb") as f:
        f.write(response.content)


if __name__ == "__main__":
    get_url("http://zjj.zhuzhou.gov.cn/c13948/")