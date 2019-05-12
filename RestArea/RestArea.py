from tkinter import *
# 민주님 코드를 보기 전에 이 주석을 꼭 봐주세요
# 제가 위치는 그냥 대략적으로 상수로 때려 박아서 나중에 고쳐야할거게요
# 이거 보시면서 place어떻게 쓰는지만 아시면 될거같아요
# place는 아주 븅신같은 친구랍니다
# 그리고 이미지 이름이 첫글자가 n이 되면 \다음에 n을 하나도 생각해요 이 븅신이 바로 \n으로 말이죠
# 그래서 _를 붙였답니다 깔까랄
# 이미지 사이즈 조절을 어떻게하는건지 모르겟어요 시부레
class RestArea:
    def food(self):
        pass

    def GasStation(self):
        pass

    def Facility(self):
        pass

    def __init__(self):
        window = Tk()
        window.title = 'ReatArea'
        window.geometry('600x800+100+0')

        # 우리 메인 로고
        RAPhoto = PhotoImage(file='resource\R.gif')
        Logo = Label(window, image=RAPhoto)
        Logo.place(x=50, y=30)

        # Gmil보내는 버튼
        mailFrame = Frame(window)
        mailFrame.place(x=400, y=50)
        mailPhoto = PhotoImage(file='resource\mail.gif')
        Button(mailFrame, image=mailPhoto).pack(side=RIGHT)

        # 검색창과 그 옆에 목록
        searchFrame = Frame(window)
        searchFrame.place(x=60, y=220, width=550, height=80)
        # 검색창
        searchBox = Entry(searchFrame, width=48)
        searchBox.place(x=0, y=0)
        # 검색 목록
        searchList = Text(searchFrame, width=27, height=50)
        searchList.place(x=320, y=0)

        # 음식점 / 주유소 / 편의시절 카테고리 버튼
        dataFrame = Frame(window)
        dataFrame.place(x=70, y=350, width=500, height=300)
        # 음식점
        categoryFood = Button(dataFrame, text="음식점", width=13, command=self.food)
        categoryFood.place(x=0, y=0)
        # 주유소
        categoryGas = Button(dataFrame, text='주유소', width=13, command=self.GasStation)
        categoryGas.place(x=100, y=0)
        # 편의시설
        categoryFacility = Button(dataFrame, text='편의시설', width=13, command=self.Facility)
        categoryFacility.place(x=200, y=0)
        # 사진
        dataPhoto = PhotoImage(file='resource\_no.png')
        dataImage = Label(dataFrame, image=dataPhoto)
        dataImage.place(x=40, y=25 + 1)
        # 목록
        dataList = Text(dataFrame)
        dataList.place(x=300 + 1, y=25 + 1)
        # 정보
        dataInfo = Text(dataFrame, width=42, height=20)
        dataInfo.place(x=0, y=150+1)

        # 이벤트 정보
        # 리스트 따로 정보따로 할거에여?
        # 우선 모르겠으니 하나로 맨글어둘게용
        eventFrame = Frame(window)
        eventFrame.place(x=70, y=700)
        eventList = Text(eventFrame, width=70, height=5)
        eventList.pack()



        window.mainloop()

RestArea()
