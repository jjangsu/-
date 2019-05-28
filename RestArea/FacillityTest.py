# ㅡ*ㅡ coding: utf8 -*-
from xml.etree import ElementTree

def findCon(ConName):
    f = open("Facility.xml", 'r', encoding='UTF8')
    data = f.read()
    # print(data)

    tree = ElementTree.fromstring(data)

    itemElements = tree.getiterator("list")

    conRoot = ElementTree.Element("data")
    # conRoot.text = '편의시설'

    # print(conRoot)
    # print(itemElements)
    for item in itemElements:
        if item.find("stdRestNm") is not None:
            tmp = item.find("stdRestNm").text
            if ConName in tmp:
                conSubRoot = ElementTree.Element("list")
                ElementTree.SubElement(conRoot, "list").text = '리스트'
                # conSubRoot = ElementTree.Element("list")
                # conSubRoot.text = '리스트'
                # conRoot.append(conSubRoot)

                if ElementTree.SubElement(conSubRoot, "psName") is not None:
                    ElementTree.SubElement(conSubRoot, "psName").text = item.find("psName").text
                    # tmpNode = ElementTree.Element("psName")
                    # tmpNode.text = item.find("psName").text
                    # # print(tmpNode.text)
                    # conSubRoot.append(tmpNode)

                if ElementTree.Element("stime") is not None:
                    tmpNode1 = ElementTree.SubElement(conSubRoot, "stime")
                    tmpNode1.text = item.find("stime").text
                    # print(tmpNode1.text)
                    conSubRoot.append(tmpNode1)

                if ElementTree.Element("etime") is not None:
                    tmpNode2 = ElementTree.SubElement(conSubRoot, "etime")
                    tmpNode2.text = item.find("etime").text
                    # print(tmpNode2.text)
                    conSubRoot.append(tmpNode2)

                if ElementTree.Element("psDesc") is not None:
                    tmpNode3 = ElementTree.SubElement(conSubRoot, "psDesc")
                    tmpNode3.text = item.find("psDesc").text
                    # print(tmpNode2.text)
                    conSubRoot.append(tmpNode3)
    ElementTree.dump(conRoot)
    print(conRoot)
    print(conSubRoot)
    # print(ElementTree.tostring(conRoot).decode(('utf-8')))
    f.close()
    return conRoot


# findCon("만남")


