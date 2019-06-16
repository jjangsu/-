# ㅡ*ㅡ coding: utf8 -*-
import urllib
import http.client
from xml.etree import ElementTree
from xml.dom.minidom import parseString
import gmail

routeNoToName = {'경부선':'0010', '남해선':'0100', '88올림픽선':'0120', '무안광주선':'0121 ', '고창담양선':'0140',
                 '서해안선': '0150  ', '평택시흥선':'0153  ', '울산선':'0160', '평택화성선':'0170', '대구포항선':'0200',
                 '익산장수선': '0201', '호남선':'0251', '천안논산선':'0252', '순천완주선':'0270', '청원상주선':'0300',
                 '당진대전선': '0301', '중부선':'0352', '제2중부선':'0370', '평택제천선':'0400', '중부내륙선':'0450', '영동선':'0500'}
# 이걸 제가 나름 노가다로 쳤는디 그지같은데 이게 안맞아요 시부레 다 부수고싶었어유
DataList = []

def routeURLBuilder(name):  # URL 만들때는 모두 이런 형식으로 만들면 될꺼같아유 이거 복붙해서 함수 이름이랑 내용만 바꿉니다
    #str = '/exopenapi/business/serviceAreaRoute?serviceKey=jyWeFegnALTcwvSFHvgeaQYIhtirRuGHTyB5YYxZNpQmWoQGf7EQc5%2F9Jsb6vw1kxdc0QhsfiT78%2BEyDQKIEyQ%3D%3D&type=xml&serviceAreaName='
    str = '/exopenapi/business/serviceAreaRoute?serviceKey=jyWeFegnALTcwvSFHvgeaQYIhtirRuGHTyB5YYxZNpQmWoQGf7EQc5%2F9Jsb6vw1kxdc0QhsfiT78%2BEyDQKIEyQ%3D%3D&type=xml&serviceAreaName='
    # str += '%EA%B8%B0%ED%9D%A5'
    hangul_utf8 = urllib.parse.quote(name)
    str += hangul_utf8
    str += '&numOfRows=10&pageNo=1'
    return str

def SelectRestAreaFacility(name):   # 파싱하는 친구에유
    # conn = http.client.HTTPConnection("data.ex.co.kr")
    conn = http.client.HTTPConnection("data.ex.co.kr")
    # hangul_utf8 = urllib.parse.quote("한국산업기술대학교")
    uri = routeURLBuilder(name)
    conn.request("GET", uri)
    req = conn.getresponse()
    #print(req.status, req.reason)
    #print(req.read().decode('utf-8'))
    print(req.status, req.reason)
    # print(req.read().decode('utf-8'))
    temp = req.read().decode(('utf-8'))
    print("-------------")
    print(temp)

    print(req.status)
    if int(req.status) == 200:
        print("Book data downloading complete!")
        print(req.read().decode(('utf-8')))

        return putXmlToSearchList(temp)   # 파싱한거를 str통체로 저 함수에 넘깁니다 return 보이죠? 저런식으로 RestArea에 값을 넘겨줘야해유 여기서 ReatArea변수에 접근할 수 없어유
    else:
        print("OpenAPI request has been failed!! please retry")
        return None


def putXmlToSearchList(strXml): # str을 그 원하는거만 찾아주는 친구에유
    returnList = []
    tree = ElementTree.fromstring(strXml)
    print(strXml)

    itemElements = tree.getiterator("list")  # return list type
    print(itemElements)
    for item in itemElements:
        tmpList = []
        name = item.find("brand")
        tmpList.append(name.text)
        name = item.find("convenience")
        tmpList.append(name.text)
        name = item.find("serviceAreaCode") #휴게소 코드 시바것
        tmpList.append(name.text)
        name = item.find("telNo")
        tmpList.append(name.text)
        name = item.find("batchMenu")
        tmpList.append(name.text)
        #gmail.sendDataList.append("야호")

        returnList.append(tmpList)
    # print(returnList)
    return returnList #여기도 이렇게 리턴해줍니더
