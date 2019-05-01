from tkinter import *
import random

class Samok:
    def endGame(self, winner):
        self.label.configure(text=winner+'우승!!!')
    def check(self):
        for r in range(6):
            for c in range(7):
                if self.buttonList[r*7+c]["text"] == '':
                    self.count = 0
                    self.temp = ''
                elif self.count == 0:
                    self.temp = self.buttonList[r*7+c]["text"]
                    self.count = 1
                else:
                    if self.buttonList[r*7+c]["text"] == self.temp:
                        self.count += 1
                        self.temp = self.buttonList[r*7+c]["text"]
                        if self.count == 4:
                            self.endGame(self.buttonList[r*7+c]["text"])
                    else:
                        self.count = 1
                        self.temp = self.buttonList[r*7+c]["text"]
            self.count = 0

                
    def again(self):
        for r in range(6):
            for c in range(7):
                self.buttonList[r*7+c].configure(text='', image=self.imageList[2], command=lambda Row=r, Col=c: self.pressed(Row,Col))
        self.turn = True
    def pressed(self,Row,Col):
        for r in range(5,-1,-1):
            if self.buttonList[r*7+Col]["text"]=='':
                if self.turn == True:   #o차례
                    self.buttonList[r*7+Col].configure(text='o', image=self.imageList[0])
                    self.label.configure(text='x차례')
                else:
                    self.buttonList[r*7+Col].configure(text='x', image=self.imageList[1])
                    self.label.configure(text='o차례')
                self.turn = not self.turn
                self.check()
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
        frame1 = Frame(window)
        frame1.pack()
        for r in range(6):
            for c in range(7):
                self.buttonList.append(Button(frame1, text='', image=self.imageList[2], command=lambda Row=r, Col=c: self.pressed(Row,Col)))
                self.buttonList[r*7+c].grid(row=r, column=c)
        frame2 = Frame(window)
        frame2.pack()
        Button(frame2, text="다시 시작",command=self.again).pack()
        self.label = Label(frame2, text='o차례')
        self.label.pack()

        window.mainloop()

Samok()