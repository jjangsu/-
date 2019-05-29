# -*- coding: utf-8 -*-
from tkinter import *
from xml.dom.minidom import parse, parseString
from test import SearchRestArea
from Facility import SelectRestAreaFacility, putXmlToSearchList
from gasStation import SelectRestAreaGas
from gmail import sendGmail
from FacillityTest import findCon
from Event import findEventByName
from Food import getAllFoodData
from Food import findFoodtByName


RestAreaList = []
FacilityList = []
FoodList = []
GasStationList = []
EventList = []
checkDataButton = 0
AllDoc = None
xmlFD = -1
RestAreaName = ''
isFirstTimeGetFood = True
buttonColor = 'lavender'
bgColor = 'thistle'
checkColor = 'pink'


class RestArea:

    def changSelectButtonColor(self):
        global checkDataButton
        if checkDataButton == 0:    #음식
            self.categoryFood.configure(background=checkColor)
            self.categoryGas.configure(background=buttonColor)
            self.categoryFacility.configure(background=buttonColor)
        elif checkDataButton == 1:  #주유소
            self.categoryFood.configure(background=buttonColor)
            self.categoryGas.configure(background=checkColor)
            self.categoryFacility.configure(background=buttonColor)
            pass
        else:                       #휴게소
            self.categoryFood.configure(background=buttonColor)
            self.categoryGas.configure(background=buttonColor)
            self.categoryFacility.configure(background=checkColor)
            pass

    def food(self):
        global checkDataButton
        global FoodList
        checkDataButton = 0
        self.ClearDataBox()
        self.changSelectButtonColor()

        FoodList = findFoodtByName(RestAreaName)

        for i in range(len(FoodList)):
            if FoodList[i] is not '':
                self.dataList.insert(i, FoodList[i][1])



    def GasStation(self):
        global checkDataButton
        checkDataButton = 1
        self.ClearDataBox()
        self.changSelectButtonColor()

        print("------------")
        print(RestAreaName)
        print(self.searchBox.get())
        GasStationList = SelectRestAreaGas(self.searchBox.get(), RestAreaName)
        print(GasStationList)

        if GasStationList is not None:
            self.dataInfo.insert(INSERT, "disel: " + GasStationList[1] + "\n")
            self.dataInfo.insert(INSERT, "gasoline: " + GasStationList[2] + "\n")
            self.dataInfo.insert(INSERT, "lpg: " + GasStationList[3] + "\n")
        else:
            self.dataInfo.insert(INSERT, "주유소 없음")


    def Facility(self):
        global checkDataButton
        global FacilityList
        global RestAreaName
        checkDataButton = 2
        self.ClearDataBox()
        self.changSelectButtonColor()

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


    def onclick_event(self, evt):
        global FoodList
        global checkDataButton
        if checkDataButton == 0:
            self.dataInfo.delete('1.0', END)
            a = evt.widget.curselection()[0]
            if FoodList[a] is not None:
                self.dataInfo.insert(INSERT, "price: " + FoodList[a][2] + "\n")
                self.dataInfo.insert(INSERT, "informaiton: " + FoodList[a][3] + "\n")

    def initDataList(self):
        # 목록
        self.dataList = Listbox(self.window, activestyle='none', width=35, height=18)
        self.dataList.bind('<<ListboxSelect>>', self.onclick_event)
        self.dataList.place(x=333, y=330)
        self.dataList.selection_clear(0, END)


    def initDataInfo(self):
        # 정보
        self.dataInfo = Text(self.window, width=40, height=5)
        self.dataInfo.place(x=50, y=550)

    def initDataCategory(self):
        global buttonColor
        # 음식점
        self.categoryFood = Button(self.window, text="음식점", width=8, command=self.food, background=buttonColor)
        self.categoryFood.place(x=50, y=300)
        # 주유소
        self.categoryGas = Button(self.window, text='주유소', width=8, command=self.GasStation, background=buttonColor)
        self.categoryGas.place(x=110, y=300)
        # 편의시설
        self.categoryFacility = Button(self.window, text='편의시설', width=8, command=self.Facility, background=buttonColor)
        self.categoryFacility.place(x=170, y=300)

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
        self.mailButton.place(x=423, y=60)
        self.mailEntry = Entry(self.window)
        self.mailEntry.place(x=395, y=140)

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
        global isFirstTimeGetFood

        iSearchIndex = self.searchList.curselection()
        str = RestAreaList[iSearchIndex[0]][0]
        str = str[0:2]
        RestAreaName = str
        print("휴게소 이름 앞 2: " + str)

        print(RestAreaList)
        if len(RestAreaList[iSearchIndex[0]]) > 1:
            self.openWebMap(RestAreaList[iSearchIndex[0]][1], RestAreaList[iSearchIndex[0]][2])

        self.printEvent(str)

        if isFirstTimeGetFood == True:
            isFirstTimeGetFood = False
            getAllFoodData()
        if checkDataButton == 0:    #음식점
            self.food()
        elif checkDataButton == 1:  #주유소
            self.GasStation()
            # self.GasStation(RestAreaName)
        else:                       #편의시설
            self.Facility()




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

        self.initEventData()
        # self.initDataPhoto(0, 0)
        self.initDataList()
        self.initDataInfo()
        self.initDataCategory()
        self.intiSendGmail()
        self.initSearchCell()
        self.window.mainloop()

