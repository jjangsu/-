import urllib
import http.client
from xml.etree import ElementTree

DataList = []
serviceAreaName = ''

routeNoToName = {'경부선':'0010', '남해선':'0100', '광주대구선':'0120', '무안광주선':'0121',
                 '서해안선': '0150',  '대구포항선':'0200',
                 '익산장수선': '0201', '호남선':'0251', '천안논산선':'0252', '논산천안선':'0252', '순천완주선':'0270', '청주영덕선':'0300',
                 '당진대전선': '0301', '중부선':'0352', '평택제천선':'0400', '중부내륙선':'0450',
                 '영동선':'0500', '중앙선' : '0550', '대구부산선':'0552', '서울양양선' : '0600', '동해선':'0650',
                 '서울외곽순환선': '1000', '남해2지선':'1040', '서천공주선':'1510', '호남지선':'2510', '중부내륙지선':'4510'
                 }

def routeURLBuilder(name):  # URL 만들때는 모두 이런 형식으로 만들면 될꺼같아유 이거 복붙해서 함수 이름이랑 내용만 바꿉니다
    # exopenapi/business/curStateStation?serviceKey=jyWeFegnALTcwvSFHvgeaQYIhtirRuGHTyB5YYxZNpQmWoQGf7EQc5%2F9Jsb6vw1kxdc0QhsfiT78%2BEyDQKIEyQ%3D%3D&type=xml&oilCompany=AD&numOfRows=10&pageNo=1
    # /exopenapi/business/curStateStation?serviceKey=jyWeFegnALTcwvSFHvgeaQYIhtirRuGHTyB5YYxZNpQmWoQGf7EQc5%2F9Jsb6vw1kxdc0QhsfiT78%2BEyDQKIEyQ%3D%3D&type=xml&oilCompany=AD&numOfRows=10&pageNo=1&routeCode=0100
    str = '/exopenapi/business/curStateStation?serviceKey=jyWeFegnALTcwvSFHvgeaQYIhtirRuGHTyB5YYxZNpQmWoQGf7EQc5%2F9Jsb6vw1kxdc0QhsfiT78%2BEyDQKIEyQ%3D%3D&type=xml'
    str += '&oilCompany=AD&numOfRows=10&pageNo=1&routeCode='
    hangul_utf8 = urllib.parse.quote(name)
    str += hangul_utf8
    return str


def SelectRestAreaGas(name, serviceName):   # 파싱하는 친구에유
    global serviceAreaName
    conn = http.client.HTTPConnection("data.ex.co.kr")
    serviceAreaName = serviceName
    # hangul_utf8 = urllib.parse.quote("한국산업기술대학교")
    # tmpName = name
    tmpName = routeNoToName.get(name)
    uri = routeURLBuilder(tmpName)
    conn.request("GET", uri)
    req = conn.getresponse()
    print(req.status, req.reason)
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
    global serviceAreaName
    returnList = []
    tree = ElementTree.fromstring(strXml)
    print(strXml)

    itemElements = tree.getiterator("list")  # return list type
    # print(itemElements)
    for item in itemElements:
        tmpList = []

        # 노선 코드 + 휴게소명 앞에 두글자? 두개 이용해서 원하는 정보 찾으면 될거같아여
        print(serviceAreaName)
        serviceAreaName = serviceAreaName[0:2]
        print(serviceAreaName)
        if serviceAreaName in item.find("serviceAreaName").text:
            name = item.find("serviceAreaName")
            tmpList.append(name.text)
            name = item.find("diselPrice")
            tmpList.append(name.text)
            name = item.find("gasolinePrice")
            tmpList.append(name.text)

            name = item.find("lpgYn")
            if name.text == 'Y':
                name = item.find("lpgPrice")
                tmpList.append(name.text)
            else:
                tmpList.append("-")

            name = item.find("telNo")
            tmpList.append(name.text)

            name = item.find("direction")
            tmpList.append(name.text)

            return tmpList


        returnList.append(tmpList)
    # print("반환 리스트 -  ", returnList)
    # return returnList #여기도 이렇게 리턴해줍니더


# SelectRestAreaGas("경부선", "서울")
