from tkinter import *
from tkinter import font
import tkinter.messagebox
from player import *
from dice import *
from ScoreConfi import *
# import ScoreConfi

basicColor = 'PaleGreen1'
selectedColor = 'PaleGreen3'
backgroundColor = 'LightSkyBlue1'
rollBasicColor = 'khaki1'
rollSelectedColor = 'khaki3'
mentColor = 'pink'

class YahtzeeBoard:
    UPPERTOTAL = 6
    UPPERBONUS = 7
    LOWERTOTAL = 15

    dice = []
    diceButtons = []
    fields = []
    finish = []
    totalScore = []

    def __init__(self):
        self.InitPayers()
        self.bottomLabel = None
        self.players = []
        self.numPalyers = 0
        self.player = 0
        self.round = 0
        self.roll = 0



        self.TOTAL = 16


    def InitPayers(self):
        self.pwindow = Tk()
        self.pwindow.configure(background=backgroundColor)
        self.TempFont = font.Font(size=16, weight='bold', family='Consolas')
        self.label = []
        self.entry = []
        self.label.append(Label(self.pwindow, text='플레이어 (박)명수', font=self.TempFont, background=backgroundColor))
        self.label[0].grid(row=0, column=0)

        for i in range(1, 11):
            self.label.append(Label(self.pwindow, text='플레이어'+str(i)+" 이름", font=self.TempFont, background=backgroundColor))
            self.label[i].grid(row=i, column=0)

        for i in range(11):
            self.entry.append(Entry(self.pwindow, font=self.TempFont))
            self.entry[i].grid(row=i, column=1)

        Button(self.pwindow, text='Yahtzee players ready !_!', font = self.TempFont, command=self.playersNames, background='CadetBlue1').grid(row=11, column=0)

        self.pwindow.mainloop()

    def playersNames(self):
        self.numPalyers = int(self.entry[0].get())

        self.players = []
        for i in range(1, self.numPalyers + 1):
            self.players.append(Player(str(self.entry[i].get())))

        self.pwindow.destroy()

        self.player = 0
        self.round = 0
        self.roll = 0
        self.TOTAL = 16
        self.bonus = 0

        self.initInterface()

    def initInterface(self):
        self.window = Tk("Yahtzee Game")
        self.window.title("Yahtzee Game")
        self.window.geometry("1600x800+0+0")
        self.window.configure(background=backgroundColor)
        self.TempFont = font.Font(size=16, weight='bold', family='Consolas')

        self.finish = [False for i in range(self.numPalyers)]
        self.totalScore = [0 for i in range(self.numPalyers)]

        for i in range(5):
            self.dice.append(Dice())
        self.scoreConfi = Configuration()

        self.rollDice = Button(self.window, text='Rock & Roll', font=self.TempFont, command=self.rollDiceListener, background=rollBasicColor)
        self.rollDice.grid(row=0, column=0)

        for i in range(5):
            self.diceButtons.append(Button(self.window, text='?', font=self.TempFont, width=8, background=basicColor, command=lambda row=i: self.diceListener(row)))
            self.diceButtons[i].grid(row=i+1, column=0)

        for i in range(self.TOTAL + 2):
            Label(self.window, text=self.scoreConfi.configs[i], font=self.TempFont, background=backgroundColor).grid(row=i, column=1)
            for j in range(self.numPalyers):
                if i == 0:
                    Label(self.window, text=self.players[j].toString(), font=self.TempFont, background=backgroundColor).grid(row=i, column=5+j)
                else:
                    if j==0:
                        self.fields.append(list())
                    self.fields[i-1].append(Button(self.window, text='', font=self.TempFont, width=8, command=lambda row=i-1: self.categoryListener(row)))
                    self.fields[i - 1][j]['bg'] = basicColor
                    self.fields[i-1][j].grid(row=i, column=5+j)

                    if j != self.player or (i-1) == self.UPPERTOTAL or (i-1) == self.UPPERBONUS or (i-1) == self.LOWERTOTAL or (i-1) == self.TOTAL:
                        self.fields[i-1][j]['state'] = 'disabled'
                        self.fields[i-1][j]['bg'] = selectedColor

        self.bottomLabel = Label(self.window, text=self.players[self.player].toString() + " 차례: Roll Dice 버튼을 누르세요", font=self.TempFont, background=mentColor) # , width=35
        self.bottomLabel.place(x=0, y=760) # grid(row=self.TOTAL+2, column=0)


    def rollDiceListener(self):
        for i in range(5):
            if self.diceButtons[i]['bg'] != selectedColor:
                self.dice[i].rollDice()
                self.diceButtons[i].configure(text=str(self.dice[i].getRoll()))

        if self.roll == 0 or self.roll == 1:
            self.roll += 1
            self.rollDice.configure(text='Rock & Roll')
            self.bottomLabel.configure(text='pick fix dice and Roll Again')
        elif self.roll == 2:
            self.bottomLabel.configure(text='Pick Category!_!')
            self.rollDice['state'] = 'disabled'
            self.rollDice['bg'] = rollSelectedColor

        for i in range(6):
            if not self.players[self.player].getUsed(i):
                tmp = self.scoreConfi.score(i, self.dice)
                self.fields[i][self.player].configure(text=str(tmp))
        for i in range(6, 13):
            if not self.players[self.player].getUsed(i):
                tmp = self.scoreConfi.score(i + 2, self.dice)
                self.fields[i + 2][self.player].configure(text=str(tmp))


    def diceListener(self, row):
        # self.diceButtons[row]['state'] = 'disabled'
        if self.diceButtons[row]['bg'] == basicColor:
            self.diceButtons[row]['bg'] = selectedColor
        else:
            self.diceButtons[row]['bg'] = basicColor


    def categoryListener(self, row):
        self.score = self.scoreConfi.score(row, self.dice)
        # print("점수 - " + str(self.score))
        index = row
        if row > 7:
            index = row - 2

        self.players[self.player].setScore(self.score, index)
        # self.players[self.player].setAtUsed(index)
        self.fields[row][self.player].configure(text=str(self.score))
        self.fields[row][self.player]['state'] = 'disabled'
        self.fields[row][self.player]['bg'] = selectedColor

        if self.players[self.player].allUpperUsed():
            self.fields[self.UPPERTOTAL][self.player].configure(text=str(self.players[self.player].getUpperScore()))
            if self.players[self.player].getUpperScore() > 63:
                self.bonus = 35
                self.fields[self.UPPERBONUS][self.player].configure(text='35')

            else:
                self.fields[self.UPPERBONUS][self.player].configure(text='0')

        if self.players[self.player].allLowerUsed():
            self.fields[15][self.player].configure(text= str(self.players[self.player].getLowerScore()))
            pass

        if self.players[self.player].allUpperUsed() and self.players[self.player].allLowerUsed():
            self.totalScore[self.player] = self.players[self.player].getUpperScore() + self.players[self.player].getLowerScore() + self.bonus
            self.fields[16][self.player].configure(text=str(self.totalScore[self.player]))
            pass

        if self.numPalyers > 1:
            for i in range(17):
                self.fields[i][self.player]['state'] = 'disabled'
                self.fields[i][self.player]['bg'] = selectedColor
            for i in range(6):
                if not self.players[self.player].getUsed(i):
                    self.fields[i][self.player]["text"] = ""
            for i in range(7):
                if not self.players[self.player].getUsed(i + 6):
                    self.fields[i + 8][self.player]["text"] = ""

        if self.player == 0:
            self.round += 1
        if self.round >= 13:
            self.finish[self.player] = True

        print(self.finish.count(True))
        if self.finish.count(True) == self.numPalyers:
            m = 0
            ii = 0
            for i in range(self.numPalyers):
                if self.totalScore[i] > m:
                    m = self.totalScore[i]
                    ii = i
            Label(self.window, text= "♬" + self.players[ii].toString() + "이(가) " + str(self.totalScore[ii]) + "점으로 이겼습니다!♬", font=self.TempFont, background=mentColor).place(x=100, y =350)


        self.player = (self.player + 1) % self.numPalyers

        for i in range(6):
            if self.fields[i][self.player]["text"] is "":
                self.fields[i][self.player]['state'] = 'normal'
                self.fields[i][self.player]['bg'] = basicColor
            elif self.numPalyers > 1:
                self.fields[i][self.player]['bg'] = selectedColor
        for i in range(8, 15):
            if self.fields[i][self.player]["text"] is "":
                self.fields[i][self.player]['state'] = 'normal'
                self.fields[i][self.player]['bg'] = basicColor
            # else:
            #     self.fields[i][self.player]['bg'] = selectedColor

        for i in range(self.TOTAL + 1):
            for j in range(self.numPalyers):
                pass

        self.roll = 0
        self.bottomLabel.configure(text='pick fix dice and Roll Again')
        self.rollDice['state'] = 'normal'
        self.rollDice['bg'] = rollBasicColor
        for i in range(5):
            self.diceButtons[i]['state'] = 'normal'
            # self.dice[i].rollDice()
            self.diceButtons[i].configure(text='?')
            self.diceButtons[i]['bg'] = basicColor



YahtzeeBoard()
