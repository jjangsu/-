# 절대 이 파일에 import로 restArea에 있는거 하면 안되유 그럼 루프를 도는지 다 터집니다
# 그래서 직접 여기서 접근하지 못하고 RestArea에서 여기있는 함수를 호출하고 리턴값으로 주는 형식으로 해야합니다
# 다른것도 파싱하려면 차라리 이 test를 복사해서 이 파일은 휴게소 선택 다른파일은 뭐 음식 이런식으로 해도 될꺼같아유
import urllib
import http.client
from xml.etree import ElementTree
routeNoToName = {'경부선':'0010', '남해선':'0100', '88올림픽선':'0120', '무안광주선':'0121 ', '고창담양선':'0140',
                 '서해안선': '0150  ', '평택시흥선':'0153  ', '울산선':'0160', '평택화성선':'0170', '대구포항선':'0200',
                 '익산장수선': '0201', '호남선':'0251', '천안논산선':'0252', '순천완주선':'0270', '청원상주선':'0300',
                 '당진대전선': '0301', '중부선':'0352', '제2중부선':'0370', '평택제천선':'0400', '중부내륙선':'0450', '영동선':'0500'}

DataList = []
#http://data.ex.co.kr/exopenapi/locationinfo/locationinfoRest?serviceKey=jyWeFegnALTcwvSFHvgeaQYIhtirRuGHTyB5YYxZNpQmWoQGf7EQc5%2F9Jsb6vw1kxdc0QhsfiT78%2BEyDQKIEyQ%3D%3D&type=xml&routeNo=0100&numOfRows=10&pageNo=1
# 편의 시설 현황
#http://data.ex.co.kr/exopenapi/business/serviceAreaRoute?serviceKey=jyWeFegnALTcwvSFHvgeaQYIhtirRuGHTyB5YYxZNpQmWoQGf7EQc5%2F9Jsb6vw1kxdc0QhsfiT78%2BEyDQKIEyQ%3D%3D&type=xml&numOfRows=10&pageNo=1
def routeURLBuilder(name):  # URL 만들때는 모두 이런 형식으로 만들면 될꺼같아유 이거 복붙해서 함수 이름이랑 내용만 바꿉니다
    str = '/exopenapi/locationinfo/locationinfoRest?serviceKey=jyWeFegnALTcwvSFHvgeaQYIhtirRuGHTyB5YYxZNpQmWoQGf7EQc5%2F9Jsb6vw1kxdc0QhsfiT78%2BEyDQKIEyQ%3D%3D&type=xml&routeNo='
    str += routeNoToName.get(name)
    str += '&numOfRows=10&pageNo=1'
    return str

def SearchRestArea(name):   # 파싱하는 친구에유
    conn = http.client.HTTPConnection("data.ex.co.kr")
    #hangul_utf8 = urllib.parse.quote("한국산업기술대학교")
    uri = routeURLBuilder(name)
    conn.request("GET", uri)
    req = conn.getresponse()
    # print(req.status, req.reason)
    #print(req.read().decode('utf-8'))

    if int(req.status) == 200:
        # print("Book data downloading complete!")
        return putXmlToSearchList(req.read())   # 파싱한거를 str통체로 저 함수에 넘깁니다 return 보이죠? 저런식으로 RestArea에 값을 넘겨줘야해유 여기서 ReatArea변수에 접근할 수 없어유
    else:
        print("OpenAPI request has been failed!! please retry")
        return None

def putXmlToSearchList(strXml): # str을 그 원하는거만 찾아주는 친구에유
    RestAreaList = []
    tree = ElementTree.fromstring(strXml)
    print (strXml)

    itemElements = tree.getiterator("list")  # return list type
    print(itemElements)
    for item in itemElements:
        tmpList = []
        name = item.find("unitName")
        tmpList.append(name.text)
        name = item.find("xValue")
        tmpList.append(name.text)
        name = item.find("yValue")
        tmpList.append(name.text)

        RestAreaList.append(tmpList)
    return RestAreaList #여기도 이렇게 리턴해줍니더
