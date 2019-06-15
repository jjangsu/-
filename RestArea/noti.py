#!/usr/bin/python
# coding=utf-8

import sys
import time
import sqlite3
import telepot
from pprint import pprint
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from datetime import date, datetime, timedelta
import traceback

routeNoToName = {'경부선':'0010', '남해선':'0100', '광주대구선':'0120', '무안광주선':'0121',
                 '서해안선': '0150',  '대구포항선':'0200',
                 '익산장수선': '0201', '호남선':'0251', '천안논산선':'0252', '논산천안선':'0252', '순천완주선':'0270', '청주영덕선':'0300',
                 '당진대전선': '0301', '중부선':'0352', '평택제천선':'0400', '중부내륙선':'0450',
                 '영동선':'0500', '중앙선' : '0550', '대구부산선':'0552', '서울양양선' : '0600', '동해선':'0650',
                 '서울외곽순환선': '1000', '남해2지선':'1040', '서천공주선':'1510', '호남지선':'2510', '중부내륙지선':'4510'
                 }

key = '	jyWeFegnALTcwvSFHvgeaQYIhtirRuGHTyB5YYxZNpQmWoQGf7EQc5%2F9Jsb6vw1kxdc0QhsfiT78%2BEyDQKIEyQ%3D%3D'
TOKEN = '744836087:AAF-tPLgcH2YpTu-_VtG-9E7V9z24yCBtoE'
MAX_MSG_LENGTH = 10
baseurl = 'http://data.ex.co.kr/exopenapi/business/curStateStation?serviceKey=jyWeFegnALTcwvSFHvgeaQYIhtirRuGHTyB5YYxZNpQmWoQGf7EQc5%2F9Jsb6vw1kxdc0QhsfiT78%2BEyDQKIEyQ%3D%3D&type=xml&oilCompany=AD&numOfRows=999&pageNo=1&routeCode='
bot = telepot.Bot(TOKEN)

def getData(areaCode):
    res_list = []
    print('**********************')
    print(areaCode)
    if routeNoToName.get(areaCode) is None:
        return
    else:
        url = baseurl+routeNoToName.get(areaCode)
        #print(routeNoToName.get(areaCode))
        print(url)
        res_body = urlopen(url).read()
        print(res_body)
        soup = BeautifulSoup(res_body, 'html.parser')
        items = soup.findAll('list')
        #print("아이템즈다")
        #print(items)
        for item in items:
            #print('**888888***')
            #print(item.text)
            cleanr = re.compile('<.*?>')
            item = re.sub(cleanr, '&', str(item))
            #print('***')
            #print(item)
            parsed = item.split('&')
            #print('*')
            #print(parsed)
            try:
                row = parsed[20]+'휴게소 - '+parsed[2]+'방향, 디젤: '+parsed[4]+', 가솔린: '+parsed[6]+', lpg: '+parsed[8]
            except IndexError:
                row = item.replace('|', ',')

            if row:
                res_list.append(row.strip())
        return res_list

def sendMessage(user, msg):
    try:
        bot.sendMessage(user, msg)
    except:
        traceback.print_exc(file=sys.stdout)

def run(date_param, param='11710'):
    conn = sqlite3.connect('logs.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS logs( user TEXT, log TEXT, PRIMARY KEY(user, log) )')
    conn.commit()

    user_cursor = sqlite3.connect('users.db').cursor()
    user_cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, location TEXT, PRIMARY KEY(user, location) )')
    user_cursor.execute('SELECT * from users')

    for data in user_cursor.fetchall():
        print(data)
        user, param = data[0], routeNoToName.get(data[1])
        print(user, date_param, param)
        res_list = getData( param )
        #print('**************************')
        #print(param)
        msg = ''
        for r in res_list:
            try:
                cursor.execute('INSERT INTO logs (user,log) VALUES ("%s", "%s")'%(user,r))
            except sqlite3.IntegrityError:
                # 이미 해당 데이터가 있다는 것을 의미합니다.
                pass
            else:
                print( str(datetime.now()).split('.')[0], r )
                if len(r+msg)+1>MAX_MSG_LENGTH:
                    sendMessage( user, msg )
                    msg = r+'\n'
                else:
                    msg += r+'\n'
        if msg:
            sendMessage( user, msg )
    conn.commit()

if __name__=='__main__':
    today = date.today()
    current_month = today.strftime('%Y%m')

    print( '[',today,']received token :', TOKEN )

    pprint( bot.getMe() )

    run(current_month)
