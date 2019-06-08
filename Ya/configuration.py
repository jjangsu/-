from dice import *

class Configuration:

    configs = ["Category","Ones", "Twos","Threes","Fours","Fives","Sixes","Upper Scores","Upper Bonus(35)","Three of a kind", "Four of a kind", "Full House(25)","Small Straight(30)", "Large Straight(40)", "Yahtzee(50)","Chance","Lower Scores", "Total"]

def getConfigs():
        return Configuration.configs

def score(row, d):
    if row >= 0 and row <= 6:
        return Configuration.scoreUpper(d, row+1)
    elif row == 8:
        pass

def scoreUpper(d, num):
    pass

def scoreThreeOfKind(d):
    pass

def scoreFourOfKind(d):
    pass

def scoreFullHouse(d):
    pass

def scoreSmallStraight(d):
    pass

def scoreLargeStraight(d):
    pass

def scoreYahtzee(d):
    pass

def sumDie(d):
    pass

