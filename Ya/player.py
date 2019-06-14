class Player:
    UPPER = 6
    LOWER = 7

    def __init__(self, name):
        self.name = name
        self.score = [0 for i in range(self.UPPER + self.LOWER)]
        self.used = [False for i in range(self.UPPER + self.LOWER)]

    def setScore(self, score, index):
        self.score[index] = score
        self.used[index] = True
        pass
    def getUpperScore(self):
        s = 0
        for i in range(6):
            s += self.score[i]
        return s
        pass

    def getLowerScore(self):
        s = 0
        for i in range(self.UPPER, self.UPPER + self.LOWER):
            s += self.score[i]
        return s
        pass
    def getUsed(self):
        pass
    def getTotalScore(self):
        pass
    def toString(self):
        return self.name

    def allUpperUsed(self):
        for i in range(self.UPPER):
            if self.used[i] == False:
                return False
        return True

    def allLowerUsed(self):
        for i in range(self.UPPER, self.UPPER + self.LOWER):
            if self.used[i] == False:
                return False
        return True