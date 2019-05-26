#http://data.ex.co.kr/exopenapi/locationinfo/locationinfoRest?serviceKey=jyWeFegnALTcwvSFHvgeaQYIhtirRuGHTyB5YYxZNpQmWoQGf7EQc5%2F9Jsb6vw1kxdc0QhsfiT78%2BEyDQKIEyQ%3D%3D&type=xml&routeNo=0100&numOfRows=10&pageNo=1

import urllib
import http.client
from xml.etree import ElementTree
from xml.dom.minidom import parse, parseString
routeNoToName = {'경부선':'0010', '남해선':'0100', '88올림픽선':'0120', '무안광주선':'0121 ', '고창담양선':'0140',
                 '서해안선': '0150  ', '평택시흥선':'0153  ', '울산선':'0160', '평택화성선':'0170', '대구포항선':'0200',
                 '익산장수선': '0201', '호남선':'0251', '천안논산선':'0252', '순천완주선':'0270', '청원상주선':'0300',
                 '당진대전선': '0301', '중부선':'0352', '제2중부선':'0370', '평택제천선':'0400', '중부내륙선':'0450', '영동선':'0500'}
DataList = []

def routeURLBuilder(name):
    str = '/exopenapi/locationinfo/locationinfoRest?serviceKey=jyWeFegnALTcwvSFHvgeaQYIhtirRuGHTyB5YYxZNpQmWoQGf7EQc5%2F9Jsb6vw1kxdc0QhsfiT78%2BEyDQKIEyQ%3D%3D&type=xml&r&routeNo='
    str += routeNoToName.get(name)
    str += '&numOfRows=10&pageNo=1'
    return str

def SearchRestArea(name):
    conn = http.client.HTTPConnection("data.ex.co.kr")
    hangul_utf8 = urllib.parse.quote("한국산업기술대학교")
    uri = routeURLBuilder(name)
    conn.request("GET", uri, None)
    req = conn.getresponse()
    #print(req.status, req.reason)
    #print(req.read().decode('utf-8'))

    print(req.status)
    if int(req.status) == 200:
        print("Book data downloading complete!")
        return putXmlToSearchList(req.read())
    else:
        print("OpenAPI request has been failed!! please retry")
        return None

def putXmlToSearchList(strXml):
    RestAreaList = []
    tree = ElementTree.fromstring(strXml)
    print (strXml)
    # Book 엘리먼트를 가져옵니다.
    itemElements = tree.getiterator("list")  # return list type
    print(itemElements)
    for item in itemElements:
        name = item.find("unitName")
        RestAreaList.append(name.text)
    return RestAreaList


#SearchRestArea()