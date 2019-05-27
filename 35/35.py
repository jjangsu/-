from tkinter import *
import numpy as np

class Samok:
    def endGame(self, winner):
        self.state = False
        self.label.configure(text=winner+'우승!!!')


    def check(self):    #가로
        for r in range(6):
            self.count = 0
            for c in range(7):
                if self.buttonList[r*7+c]["text"] == '':
                    self.count = 1
                    self.temp = ''
                elif self.count == 0 and self.buttonList[r*7+c]["text"] != '':
                    self.temp = self.buttonList[r*7+c]["text"]
                    self.count = 1
                else:
                    if self.buttonList[r*7+c]["text"] == self.temp:
                        self.count += 1
                        self.temp = self.buttonList[r*7+c]["text"]
                        if self.count >= 4:
                            self.endGame(self.buttonList[r*7+c]["text"])
                    else:
                        self.count = 1
                        self.temp = self.buttonList[r*7+c]["text"]


            for r in range(6, -1, -1):  #세로
                self.count = 1
                self.temp = ''
                # print("--------")
                for c in range(5, -1, -1):
                    if self.buttonList[c*7+r]["text"] != '':
                        self.temp = self.buttonList[c*7+r]["text"]
                        if self.temp == self.buttonList[(c - 1)*7+r]["text"]:
                                self.count += 1
                        else:
                                self.count = 1
                    if self.count >= 4:
                        self.endGame(self.temp)

            # 대각선
            # self.crossCheck()

    def crossCheck(self, ori_x, ori_y):
        slashFrom, slashTo = 0, 0

        # 오 위
        x, y = ori_x - 1, ori_y + 1
        while x >= 0 and y < 6:
            if self.buttonList[y * 7 + x]['text'] == self.buttonList[ori_y * 7 + ori_x]['text']:
                slashFrom += 1
                x -= 1
                y += 1
            else:
                break
        x, y = ori_x + 1, ori_y - 1
        while x < 7 and y >= 0:
            if self.buttonList[y * 7 + x]['text'] == self.buttonList[ori_y * 7 + ori_x]['text']:
                slashTo += 1
                x += 1
                y -= 1
            else:
                break
        if slashFrom + slashTo >= 3:
            self.endGame(self.buttonList[ori_y*7+ori_x]["text"])
            return 0

        # 오 아
        backslashFrom, backslashTo = 0, 0
        x, y = ori_x - 1, ori_y - 1
        while x >= 0 and y >= 0:
            if self.buttonList[y * 7 + x]['text'] == self.buttonList[ori_y * 7 + ori_x]['text']:
                backslashFrom += 1
                x -= 1
                y -= 1
            else:
                break
        x, y = ori_x + 1, ori_y + 1
        while x < 7 and y < 6:
            if self.buttonList[y * 7 + x]['text'] == self.buttonList[ori_y * 7 + ori_x]['text']:
                backslashTo += 1
                x += 1
                y += 1
            else:
                break
        if backslashFrom + backslashTo >= 3:
            self.endGame(self.buttonList[ori_y*7+ori_x]["text"])
            return 0
        pass

                
    def again(self):
        self.turn = True
        self.state = True
        self.label.configure(text="o차례")
        for r in range(6):
            for c in range(7):
                self.buttonList[r*7+c].configure(text='', image=self.imageList[2], command=lambda Row=r, Col=c: self.pressed(Row,Col))
        # self.turn = True
    def pressed(self,Row,Col):
        for r in range(5, -1, -1):
            if self.buttonList[r*7+Col]["text"]=='' and self.state:
                if self.turn == True:   #o차례
                    self.buttonList[r*7+Col].configure(text='o', image=self.imageList[0])
                    self.label.configure(text='x차례')
                else:
                    self.buttonList[r*7+Col].configure(text='x', image=self.imageList[1])
                    self.label.configure(text='o차례')
                self.turn = not self.turn
                self.check()
                self.crossCheck(Col, r)
                break

    def __init__(self):
        window = Tk()
        self.turn = True
        self.imageList = []
        self.imageList.append(PhotoImage(file="image/o.gif"))
        self.imageList.append(PhotoImage(file="image/x.gif"))
        self.imageList.append(PhotoImage(file="image/empty.gif"))
        self.buttonList = []
        self.count = 0
        self.checkList = ['o', 'x']
        self.temp = 'o'

        self.state = True
        frame1 = Frame(window)
        frame1.pack()
        for r in range(6):
            for c in range(7):
                self.buttonList.append(Button(frame1, text='', image=self.imageList[2], command=lambda Row=r, Col=c: self.pressed(Row, Col)))
                self.buttonList[r*7+c].grid(row=r, column=c)
        frame2 = Frame(window)
        frame2.pack()
        Button(frame2, text="다시 시작",command=self.again).pack()
        self.label = Label(frame2, text='o차례')
        self.label.pack()

        window.mainloop()

Samok()