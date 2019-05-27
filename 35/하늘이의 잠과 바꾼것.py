def checkGameEnd(self, ori_y, ori_x):
    backslashFrom, backslashTo = 0, 0
    slashFrom, slashTo = 0, 0
    horiFrom, horiTo = 0, 0
    vertFrom, vertTo = 0, 0

    # hori
    x, y = ori_x - 1, ori_y
    while x >= 0:
        if self.buttonList[y * 7 + x]['text'] == self.buttonList[ori_y * 7 + ori_x]['text']:
            horiFrom += 1
            x -= 1
        else:
            break
    x, y = ori_x + 1, ori_y
    while x < 7:
        if self.buttonList[y * 7 + x]['text'] == self.buttonList[ori_y * 7 + ori_x]['text']:
            horiTo += 1
            x += 1
        else:
            break
    if horiFrom + horiTo >= 3:
        return True

    # vert
    x, y = ori_x, ori_y - 1
    while y >= 0:
        if self.buttonList[y * 7 + x]['text'] == self.buttonList[ori_y * 7 + ori_x]['text']:
            vertFrom += 1
            y -= 1
        else:
            break
    x, y = ori_x, ori_y + 1
    while y < 6:
        if self.buttonList[y * 7 + x]['text'] == self.buttonList[ori_y * 7 + ori_x]['text']:
            vertTo += 1
            y += 1
        else:
            break
    if vertFrom + vertTo >= 3:
        return True

    # backslash
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
        return True

    # slash
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
        return True

    return False