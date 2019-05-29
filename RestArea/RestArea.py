# -*- coding: utf-8 -*-
from tkinter import *
from xml.dom.minidom import parse, parseString
from test import SearchRestArea
from Facility import SelectRestAreaFacility, putXmlToSearchList
from gasStation import SelectRestAreaGas
from gmail import sendGmail
from FacillityTest import findCon
from Event import findEventByName


RestAreaList = []
FacilityList = []
GasStationList = []
EventList = []
checkDataButton = 0
AllDoc = None
xmlFD = -1
RestAreaName = ''
buttonColor = 'lavender'
bgColor = 'thistle'

class RestArea:

    def food(self):
        global checkDataButton
        checkDataButton = 0
        self.ClearDataBox()

    def GasStation(self):
        global checkDataButton
        checkDataButton = 1
        self.ClearDataBox()

        print("------------")
        print(RestAreaName)
        print(self.searchBox.get())
        GasStationList = SelectRestAreaGas(self.searchBox.get(), RestAreaName)
        print(GasStationList)
        for item in GasStationList:
            self.dataInfo.insert(INSERT, "disel: " + item[1] + "\n")
            self.dataInfo.insert(INSERT, "gasoline: " + item[2] + "\n")
            # self.dataInfo.insert(INSERT, "lpg: " + item[3] + "\n")


    def Facility(self):
        global checkDataButton
        global FacilityList
        global RestAreaName
        checkDataButton = 2
        self.ClearDataBox()

        FacilityList.clear()
        FacilityList = SelectRestAreaFacility(RestAreaName)

        convenienceList = []
        for data in FacilityList:
            if data[1] is not None:
                tmp = data[1].split('|')
                # print(convenienceList)
                self.dataInfo.insert(INSERT, "전화번호: " + data[3] + "\n")
                self.dataInfo.insert(INSERT, "대표 메뉴: " + data[4] + "\n")
                self.dataInfo.insert(INSERT, "브랜드: " + data[0] + "\n")
                for item in tmp:
                    if item is not '' and item not in convenienceList:
                        convenienceList.append(item)
                # print(convenienceList)
        for i in range(len(convenienceList)):
            if convenienceList[i] is not '':
                # if convenienceList[i] not in self.dataList:
                self.dataList.insert(i, convenienceList[i])

    def showData(self): #이제 여기서 일을 쫌 해야겠죠
        global checkDataButton
        if checkDataButton == 0:    #음식점
            pass
        elif checkDataButton == 1:  #주유소
            pass
        else:                       #편의시설
            pass


    def openWebMap(self, x, y):
        # 사진
        import folium
        import webbrowser
        print(x)
        print(y)
        map_osm = folium.Map(location=[float(y), float(x)], zoom_start=30)
        folium.Marker([float(y), float(x)]).add_to(map_osm)

        map_osm.save('osm.html')

        webbrowser.open('osm.html')



    def initDataList(self):
        # 목록
        self.dataList = Listbox(self.window, activestyle='none', width=35, height=18)
        self.dataList.place(x=333, y=330)

    def initDataInfo(self):
        # 정보
        self.dataInfo = Text(self.window, width=40, height=5)
        self.dataInfo.place(x=50, y=550)

    def initDataCategory(self):
        global buttonColor
        # 음식점
        categoryFood = Button(self.window, text="음식점", width=8, command=self.food, background=buttonColor)
        categoryFood.place(x=50, y=300)
        # 주유소
        categoryGas = Button(self.window, text='주유소', width=8, command=self.GasStation, background=buttonColor)
        categoryGas.place(x=110, y=300)
        # 편의시설
        categoryFacility = Button(self.window, text='편의시설', width=8, command=self.Facility, background=buttonColor)
        categoryFacility.place(x=170, y=300)

    def initEventData(self):
        self.eventList = Text(self.window, width=75, height=5)
        self.eventList.place(x=50, y=650)

    def printEvent(self, name):
        global EventList
        if EventList is not None:
            EventList.clear()
        EventList = findEventByName(name)
        self.eventList.delete('1.0',END)
        if EventList is not None:
            self.eventList.insert(INSERT, EventList)
        else:
            self.eventList.insert(INSERT, "이벤트 없음")

    def sendMail(self):
        rv = self.mailEntry.get()
        sendGmail(rv)

    def intiSendGmail(self):
        # Gmail보내는 버튼
        self.mailPhoto = PhotoImage(file='resource\_newMail.png')
        self.mailButton = Button(self.window, image=self.mailPhoto, command=self.sendMail, background=bgColor, activebackground='red')
        self.mailButton.place(x=400, y=100)
        self.mailEntry = Entry(self.window)
        self.mailEntry.place(x=375, y=170)

    def SearchRestAreaByName(self): #함수를 한번에 못넘기겠어서 만든 친굽니다 그 옆에 휴게소 목록 리스트 초기화하고 다시 받아서 넣어줍니다
        global RestAreaList
        if RestAreaList is not None:
            RestAreaList.clear()
        # print(self.searchBox.get())
        RestAreaList = SearchRestArea(self.searchBox.get())
        print(RestAreaList)
        if RestAreaList is not None:
            for i in range(len(RestAreaList)):
               self.searchList.insert(i,RestAreaList[i][0])


    def ClearDataBox(self):
        self.dataList.delete(0, self.dataList.size())
        self.dataInfo.delete('1.0', END)

    def SelectRestArea(self):
        global checkDataButton
        global RestAreaList
        global FacilityList
        global RestAreaName

        iSearchIndex = self.searchList.curselection()
        str = RestAreaList[iSearchIndex[0]][0]
        str = str[0:2]
        RestAreaName = str
        print("휴게소 이름 앞 2: " + str)

        print(RestAreaList)
        if len(RestAreaList[iSearchIndex[0]]) > 1:
            self.openWebMap(RestAreaList[iSearchIndex[0]][1], RestAreaList[iSearchIndex[0]][2])

        self.printEvent(str)
        if checkDataButton == 0:    #음식점
            self.food()
        elif checkDataButton == 1:  #주유소
            self.GasStation(RestAreaName)
        else:                       #편의시설
            self.Facility()
        # tmp = findCon(str)
        # print("------")
        # print(tmp.find("psName").text)




    def initSearchCell(self):
        # 검색창과 그 옆에 목록
        # 검색창
        self.searchBox = Entry(self.window, width=30)
        self.searchBox.place(x=50, y=220)

        Button(self.window, text='search', command=self.SearchRestAreaByName, background=buttonColor).place(x=265, y=220)
        # 검색 목록
        #self.searchList = Text(self.window, width=30, height=5)
        self.searchList = Listbox(self.window, width=30, height=5)
        self.searchList.place(x=320, y=220)
        Button(self.window, text='select', command=self.SelectRestArea, background=buttonColor).place(x=535, y=220)


    def __init__(self):
        #global restArea
        #restArea = self

        self.window = Tk()
        self.window.title = 'ReatArea'
        self.window.geometry('600x750+500+0')
        self.window.configure(background=bgColor)
        # lemon chiffon  RosyBrown1 개이쁜 핑크임   thistle 개이쁜 보라색
        # 낫밷 powder blue

        # 우리 메인 로고


        # Image.open
        self.RAPhoto = PhotoImage(file='resource\logolegoApng.png')
        Logo = Label(self.window, image=self.RAPhoto, background=bgColor)
        Logo.place(x=50, y=30)

        #self.LoadXMLFromFile()
        self.initEventData()
        # self.initDataPhoto(0, 0)
        self.initDataList()
        self.initDataInfo()
        self.initDataCategory()
        self.intiSendGmail()
        self.initSearchCell()
        self.window.mainloop()

