# author:杨森
# date: 2019/10/29 18:53
# file_name: 携程案例1
# post的另外一种请求方式payload content-Type 是json格式
import requests
import time
import json
# 设置请求地址
url = "https://flights.ctrip.com/itinerary/api/12808/products"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
    "content-type": "application/json",
    "referer": "https://flights.ctrip.com/itinerary/roundtrip/bjs-can?date=2019-11-05,2019-11-14",
    "cookie":"_abtest_userid=33004d23-fe09-4022-85fc-30c86412ebd9; DomesticUserHostCity=CGO|%d6%a3%d6%dd; gad_city=01e2fcd36d1bc003f51f35eff054dab1; _RF1=123.160.225.78; _RSG=0qaRyEjbMZCHuxTQi8o7oB; _RDG=28a796230648ab27252cfb283c03907036; _RGUID=c8d696d3-bc6e-4d00-bc87-c88b1a77be11; _ga=GA1.2.1782294538.1572339668; _gid=GA1.2.105926382.1572339668; MKT_Pagesource=PC; appFloatCnt=1; _bfa=1.1572339661875.2uikq3.1.1572339661875.1572346554380.2.9; _bfs=1.1; _gat=1; _jzqco=%7C%7C%7C%7C1572339668230%7C1.792345517.1572339667970.1572339718558.1572346556833.1572339718558.1572346556833.undefined.0.0.5.5; __zpspc=9.2.1572346556.1572346556.1%234%7C%7C%7C%7C%7C%23; _bfi=p1%3D10320673304%26p2%3D10320673302%26v1%3D9%26v2%3D8",
}
payload_data = {
"flightWay": "Roundtrip",
"classType": "ALL",
"hasChild": False,
"hasBaby": False,
"searchIndex": 1,
"airportParams":
    [
        {"dcity": "BJS",
         "acity": "CAN",
        "acityid": 1,
         "dcityname": "北京",
         "acityname": "广州",
         "dcityid": 32,
         "date": "2019-11-05"},
        {
        "acity": "CAN",
        "acityid": 32,
        "acityname": "广州",
        "date": "2019-11-05",
        "dcity": "BJS",
        "dcityid": 1,
        "dcityname": "北京"
        }
    ],
    "token": "54366eaa95b469cf6fc6f8282c3acb56"


}
reponses = requests.post(url,data=json.dumps(payload_data),headers=headers)
# 反序列化为字典
result = reponses.json()
print(type(result))
all_data = result["data"]["routeList"]
for each_data in all_data:
    # print(each_data)
    flightid = each_data['legs'][0]['flightId']
    print(flightid)
    flightNumber = each_data["legs"][0]['flight']['flightNumber']
    print(flightNumber)
    airlineName = each_data['legs'][0]['flight']['airlineName']
    print(airlineName)