from http.client import HTTPSConnection
from http.server import BaseHTTPRequestHandler, HTTPServer
import MakeHtml

conn = None
client_key = "	jyWeFegnALTcwvSFHvgeaQYIhtirRuGHTyB5YYxZNpQmWoQGf7EQc5%2F9Jsb6vw1kxdc0QhsfiT78%2BEyDQKIEyQ%3D%3D"

# 공공 데이터 포털 접속 정보
sever = "www.data.go.kr"

host = "smtp.gmail.com"
port = "587"

def userURIBuilder(uri, **user):
    str = uri + "?"
    for key in user.keys():
        str += key + "=" + user[key] + "&"
    return str


def connectOpenAPIServer():
    global conn, server
    conn = HTTPSConnection(server)
    conn.set_debuglevel(1)


def getBookDataFromISBN(isbn):
    global server, conn, client_ID, client_secret
    if conn == None:
        connectOpenAPIServer()
    uri = userURIBuilder("/v1/search/book_adv.xml", display="1", start="1", d_isbn=isbn)
    conn.request("GET", uri, None, {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret})

    req = conn.getresponse()
    print(req.status)
    if int(req.status) == 200:
        print("Book data downloading complete!")
        return extractBookData(req.read())
    else:
        print("OpenAPI request has been failed!! please retry")
        return None


def extractBookData(strXml):
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(strXml)
    print (strXml)
    # Book 엘리먼트를 가져옵니다.
    itemElements = tree.getiterator("item")  # return list type
    print(itemElements)
    for item in itemElements:
        isbn = item.find("isbn")
        strTitle = item.find("title")
        print (strTitle)
        if len(strTitle.text) > 0 :
           return {"ISBN":isbn.text,"title":strTitle.text}

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        from urllib.parse import urlparse
        import sys

        parts = urlparse(self.path)
        keyword, value = parts.query.split('=', 1)

        if keyword == "title":
            html = MakeHtmlDoc(SearchBookTitle(value))  # keyword에 해당하는 책을 검색해서 HTML로 전환합니다.
            ##헤더 부분을 작성.
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html.encode('utf-8'))  # 본분( body ) 부분을 출력 합니다.
        else:
            self.send_error(400, ' bad requst : please check the your url')  # 잘 못된 요청라는 에러를 응답한다.


def startWebService():
    try:
        server = HTTPServer(('localhost', 8080), MyHandler)
        print("started http server....")
        server.serve_forever()

    except KeyboardInterrupt:
        print("shutdown web server")
        server.socket.close()  # server 종료합니다.


def checkConnection():
    global conn
    if conn == None:
        print("Error : connection is fail")
        return False
    return True