def checkConditionX(self, dir, x):
    if dir == -1:
        return x >= 0
    elif dir == 1:
        return x < 7
    else:
        return True


def checkConditionY(self, dir, y):
    if dir == -1:
        return y >= 0
    elif dir == 1:
        return y < 6
    else:
        return True


def checkStone(self, ori_x, ori_y, dir_x, dir_y):
    x, y = ori_x + dir_x, ori_y + dir_y
    cnt = 0
    while self.checkConditionX(dir_x, x) and self.checkConditionY(dir_y, y):
        if self.buttonList[y * 7 + x]['text'] == self.buttonList[ori_y * 7 + ori_x]['text']:
            cnt += 1
            x += dir_x
            y += dir_y
        else:
            break
    return cnt


def checkGameEnd(self, ori_y, ori_x):
    li = [(-1, 0), (0, -1), (-1, -1), (1, -1)]
    for d in li:
        if self.checkStone(ori_x, ori_y, d[0], d[1]) + self.checkStone(ori_x, ori_y, -d[0], -d[1]) >= 3:
            return True
    return False