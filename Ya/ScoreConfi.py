from dice import *

class Configuration:

    def __init__(self):
        self.configs = ["Category","Ones", "Twos","Threes","Fours","Fives","Sixes","Upper Scores","Upper Bonus(35)","Three of a kind", "Four of a kind", "Full House(25)","Small Straight(30)", "Large Straight(40)", "Yahtzee(50)","Chance","Lower Scores", "Total"]

    def getConfigs(self):
            return self.configs

    def score(self, row, d):
        s = 0
        if row >= 0 and row < 6:
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
        if row == 14:
            s = self.scoreChance(d)
        return s

    def scoreUpper(self, dice, num):
        cnt = 0
        for i in range(len(dice)):
            if dice[i].getRoll() == num:
                cnt = cnt + num
        return cnt
        pass

    def scoreThreeOfKind(self, dice):
        sum = 0
        for i in range(1, 6 + 1):
            cnt = 0
            for j in range(5):
                if i == dice[j].getRoll():
                    cnt += 1
                if cnt >= 3:
                    for a in range(5):
                        sum += dice[a].getRoll()
                    return sum
        return 0
        pass

    def scoreFourOfKind(self, dice):
        sum = 0
        for i in range(1, 6 + 1):
            cnt = 0
            for j in range(5):
                if i == dice[j].getRoll():
                    cnt += 1
                if cnt >= 4:
                    for a in range(5):
                        sum += dice[a].getRoll()
                    return sum

        return 0
        pass

    def scoreFullHouse(self, dice):
        tmp = []
        for i in range(5):
            tmp.append(dice[i].getRoll())
        if tmp.count(0) == 5:
            return 0
        tmp.sort()
        first = False
        second = False
        if tmp[0] == tmp[1]:
            first = True
            if tmp[2] == tmp[3] and tmp[3] == tmp[4]:
                second = True
        if tmp[0] == tmp[1] and tmp[1] == tmp[2]:
            first = True
            if tmp[3] == tmp[4]:
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
        tmp2 = list(set(tmp))
        if len(tmp2) == 4:
            if tmp2[3] - tmp2[0] == 3:
                return 30
        # sum2 = 0
        if len(tmp2) > 4:
            if tmp2[3] - tmp2[0] == 3:
                return 30
            if tmp2[4] - tmp2[1] == 3:
                return 30

        return 0
        pass

    def scoreLargeStraight(self, dice):
        tmp = []
        for i in range(5):
            tmp.append(dice[i].getRoll())
        tmp.sort()
        tmp2 = list(set(tmp))
        # sum = 0
        if len(tmp2) > 4:
            if tmp2[4] - tmp2[0] == 4:
                return 40
            # for i in range(0, 4):
            #     sum = sum + tmp2[i + 1] - tmp2[i]
            #     if sum == 4:
            #         return 40
        return 0
        pass

    def scoreYahtzee(self, dice):
        t = []
        for i in range(5):
            t.append(dice[i].getRoll())
        if t.count(0) == 5:
            return 0
        num = dice[0].getRoll()
        # check = True
        for i in range(0, 5):
            if num != dice[i].getRoll():
                return 0
            else:
                check = True
        if check:
            return 50
        pass

    def scoreChance(self, dice):
        sum = 0
        for i in range(len(dice)):
            sum += dice[i].getRoll()
        return sum
        pass

    def sumDie(self, d):
        pass

