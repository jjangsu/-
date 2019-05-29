# ㅡ*ㅡ coding: utf8 -*-
import http.client
from xml.etree import ElementTree

foods = []  #여기에 데이터 다 들어있음

def URLBuilder(num):
    strr = '/exopenapi/restinfo/restBestfoodList?serviceKey=jyWeFegnALTcwvSFHvgeaQYIhtirRuGHTyB5YYxZNpQmWoQGf7EQc5%2F9Jsb6vw1kxdc0QhsfiT78%2BEyDQKIEyQ%3D%3D&pageNo='
    strr += str(num)
    strr += '&numOfRows=999&type=xml'
    return strr

def getAllFoodData():
    global foods
    for i in range(33):
        conn = http.client.HTTPConnection("data.ex.co.kr")
        uri = URLBuilder(i+1)
        conn.request("GET", uri, None)
        req = conn.getresponse()

        temp = req.read().decode(('utf-8'))
        if int(req.status) == 200:
            print("200 ok!")
            putXmlToSearchListAll(temp)
        else:
            return None
    #print(foods[10][1])

def findFoodtByName(name):
    global foods
    returnlist = []
    for item in foods:
        if name in item[0]:
            returnlist.append(item)

    #print(returnlist)
    return returnlist



def putXmlToSearchListAll(strXml): # str을 그 원하는거만 찾아주는 친구에유
    global foods
    food = []

    tree = ElementTree.fromstring(strXml)
    itemElements = tree.getiterator("list")  # return list type
    for item in itemElements:
        temp = item.find("stdRestNm").text  #휴게소 이름
        food.append(temp)
        temp = item.find("foodNm").text     # 음식 이름
        food.append(temp)
        temp = item.find("foodCost").text  # 음식 가격
        food.append(temp)
        if item.find("etc") is not None:
            temp = item.find("etc").text  # 음식 설명
            food.append(temp)
        else:
            food.append('none')
        foods.append(food[:])
        food.clear()
    #return foods #여기도 이렇게 리턴해줍니더

#getAllFoodData()
#findFoodtByName('부산')




