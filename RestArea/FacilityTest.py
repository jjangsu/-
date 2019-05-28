# ㅡ*ㅡ coding: utf8 -*-
from xml.etree import ElementTree

def findCon(ConName):
    f = open("Facility.xml", 'r', encoding='UTF8')
    data = f.read()
    # print(data)

    tree = ElementTree.fromstring(data)

    itemElements = tree.getiterator("list")

    conList =[]
    # print(itemElements)
    for item in itemElements:
        if item.find("stdRestNm") is not None:
            tmp = item.find("stdRestNm").text
            if ConName in tmp:
                # conList.append()
                pass
            # if item.find("psDesc") is not None:
            #     name = item.find("psDesc")
            #     print(name)
            #     conList.append(name.text)
    print(conList)
    f.close()


findCon("서울만남")


