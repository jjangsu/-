# -*- coding: utf-8 -*-
import mimetypes
import mysmtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from http.client import HTTPSConnection
from http.server import BaseHTTPRequestHandler, HTTPServer

sendDataList = []

#global value
host = "smtp.gmail.com" # Gmail STMP 서버 주소.
port = "587"
htmlFileName = "logo.html"

senderAddr = "min164337@gmail.com"     # 보내는 사람 email 주소.
recipientAddr = "minf0723@naver.com"   # 받는 사람 email 주소.

msg = MIMEBase("multipart", "alternative")
msg['Subject'] = "Test email in Python 3.0"
msg['From'] = senderAddr
msg['To'] = recipientAddr

# MIME 문서를 생성합니다.
#htmlFD = open(htmlFileName, 'rb')
#HtmlPart = MIMEText(htmlFD.read(),'html', _charset = 'UTF-8' )
#htmlFD.close()

def sendGmail(rv, lst):
    global host, port
    html = ""
    title = 'RestArea'
    senderAddr = 'min164337@gmail.com'
    recipientAddr = rv
    #msgtext = 'tteexxtt'
    passwd = '88088808!a'
    msgtext = 'y'

    if msgtext == 'y' :
        keyword = str(lst)
        #html = MakeHtmlDoc(SearchBookTitle(keyword))
        # html = 'hello'
        for s in sendDataList:
            for item in s:
                html = html + item
                # html += "\n"
            html += " / "
            # 메일 보내면 시부레것 엔터가 안되네 
        print(html)


    import mysmtplib
    # MIMEMultipart의 MIME을 생성합니다.
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    #Message container를 생성합니다.
    msg = MIMEMultipart('alternative')

    #set message
    msg['Subject'] = title
    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    #msgPart = MIMEText(msgtext, 'plain')
    sendData = MIMEText(html, 'html', _charset = 'UTF-8')

    # 메세지에 생성한 MIME 문서를 첨부합니다.
    #msg.attach(lst)
    msg.attach(sendData)

    print ("connect smtp server ... ")
    s = mysmtplib.MySMTP(host,port)
    #s.set_debuglevel(1)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(senderAddr, passwd)    # 로긴을 합니다.
    s.sendmail(senderAddr, [recipientAddr], msg.as_string())
    s.close()

    print ("Mail sending complete!!!")