# ㅡ*ㅡ coding: utf8 -*-
import http.client
from xml.etree import ElementTree

def URLBuilder(num):
    strr = '/exopenapi/restinfo/restEventList?serviceKey=jyWeFegnALTcwvSFHvgeaQYIhtirRuGHTyB5YYxZNpQmWoQGf7EQc5%2F9Jsb6vw1kxdc0QhsfiT78%2BEyDQKIEyQ%3D%3D&pageNo='
    strr += str(num)
    strr += '&numOfRows=100&type=xml'
    return strr

def getAllEventData():
    pass

def findEventByName(name):
    #getAllEventData()
    for i in range(6):
        conn = http.client.HTTPConnection("data.ex.co.kr")
        uri = URLBuilder(i+1)
        conn.request("GET", uri, None)
        req = conn.getresponse()
        #print(req.status, req.reason)

        temp = req.read().decode(('utf-8'))
        #print("-------------")
        #print(temp)

        # print(req.status)
        if int(req.status) == 200:
            # print("Book data downloading complete!")
            #print(req.read().decode(('utf-8')))
            tt = putXmlToSearchList(temp, name)  # 파싱한거를 str통체로 저 함수에 넘깁니다 return 보이죠? 저런식으로 RestArea에 값을 넘겨줘야해유 여기서 ReatArea변수에 접근할 수 없어유
            if len(tt) != 0:
                return tt
        else:
            # print("OpenAPI request has been failed!! please retry")
            return None


def putXmlToSearchList(strXml, name): # str을 그 원하는거만 찾아주는 친구에유
    returnList = []
    tree = ElementTree.fromstring(strXml)
    #print (strXml)

    itemElements = tree.getiterator("list")  # return list type
    #print(itemElements)
    for item in itemElements:
        if item.find("stdRestNm") != None:
            temp = item.find("stdRestNm").text
            if name in temp:
                event = item.find("eventDetail")
                returnList.append(event.text)
    if len(returnList) != 0:
        # print('*******************')
        print(returnList)
    return returnList #여기도 이렇게 리턴해줍니더




