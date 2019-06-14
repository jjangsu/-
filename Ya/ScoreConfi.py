from dice import *

class Configuration:

    def __init__(self):
        self.configs = ["Category","Ones", "Twos","Threes","Fours","Fives","Sixes","Upper Scores","Upper Bonus(35)","Three of a kind", "Four of a kind", "Full House(25)","Small Straight(30)", "Large Straight(40)", "Yahtzee(50)","Chance","Lower Scores", "Total"]

    def getConfigs(self):
            return self.configs

    def score(self, row, d):
        s = 0
        if row >= 0 and row <= 6:
            return self.scoreUpper(d, row + 1)
        if row == 8:
            s = self.scoreThreeOfKind(d)
        if row == 9:
            s = self.scoreFourOfKind(d)
        if row == 10:
            s = self.scoreFullHouse(d)
        if row == 11:
            s = self.scoreSmallStraight(d)
        if row == 12:
            s = self.scoreLargeStraight(d)
        if row == 13:
            s = self.scoreYahtzee(d)
        return s



    def scoreUpper(self, dice, num):
        cnt = 0
        for i in range(len(dice)):
            if dice[i].getRoll() == num:
                cnt = cnt + num
        return cnt
        pass

    def scoreThreeOfKind(self, dice):
        for i in range(1, 6 + 1):
            cnt = 0
            for j in range(5):
                if i == dice[j].getRoll():
                    cnt += 1
                    print(cnt)
                if cnt >= 3:
                    return 17
        return 0
        pass

    def scoreFourOfKind(self, dice):
        for i in range(1, 6 + 1):
            cnt = 0
            for j in range(5):
                if i == dice[j].getRoll():
                    cnt += 1
                    print(cnt)
                if cnt >= 4:
                    return 24

        return 0
        pass

    def scoreFullHouse(self, dice):
        tmp = []
        for i in range(5):
            tmp.append(dice[i].getRoll())
        tmp.sort()
        first = False
        second = False
        if tmp[0] == tmp[1]:
            first = True
        if tmp[2] == tmp[3] and tmp[3] == tmp[4]:
            second = True
        if first and second:
            return 25
        return 0
        pass

    def scoreSmallStraight(self, dice):
        tmp = []
        for i in range(5):
            tmp.append(dice[i].getRoll())
        tmp.sort()
        print(tmp)
        tmp2 = list(set(tmp))
        print(tmp2)
        sum = 0
        sum2 = 0
        if len(tmp2) >= 4:
            for i in range(3):
                sum = sum + tmp2[i + 1] - tmp2[i]
                sum2 = sum2 + tmp2[i + 2] - tmp2[i + 1]
                if sum >= 3:
                    return 30
                if sum2 >= 3:
                    return 30

        return 0
        pass

    def scoreLargeStraight(self, dice):
        tmp = []
        for i in range(5):
            tmp.append(dice[i].getRoll())
        tmp.sort()
        tmp2 = list(set(tmp))
        sum = 0
        if len(tmp2) >= 5:
            for i in range(4):
                sum = sum + tmp2[i + 1] - tmp2[i]
                if sum >= 4:
                    return 40
        return 0
        pass

    def scoreYahtzee(self, dice):
        num = dice[0].getRoll()
        check = True
        for i in range(1, 5):
            if num != dice[i].getRoll():
                check = False
        if check:
            return 50
        else:
            return 0
        pass

    def sumDie(self, d):
        pass

