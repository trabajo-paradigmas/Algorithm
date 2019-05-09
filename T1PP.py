import match
import visual
import math
import copy


def showPointList(l):
    for i in range(len(l)):
        print("(" + str(l[i].x) + ", " + str(l[i].y) + ", " + str(l[i].color) + ")")


def aparear(n):
    P = match.create_random_points(n)
    rectangulos = []
    showPointList(P)
    aparear = [0] * len(P)
    P.sort(key=lambda Point: Point.x)
    print("Arreglo ordenado")
    showPointList(P)
    lCopy = copy.deepcopy(P)
    print("Copia de arreglo ordenado")
    showPointList(lCopy)
    rectangulos += algorithm(lCopy, aparear)
    for i in range(len(aparear)):
        print(str(aparear[i]))
    for i in rectangulos:
        print(str(i.left) + " " + str(i.right) + " " + str(i.top) + " " + str(i.bottom))
    visual.Window(points=P, rectangles=rectangulos)


def restriccion(A, B, ListO, p, q):
    for i in range(p, q):
        if (((A.x < ListO[i].x and B.x > ListO[i].x) and (A.y > ListO[i].y and B.y < ListO[i].y)) or (
                (A.x < ListO[i].x and B.x > ListO[i].x) and (A.y < ListO[i].y and B.y > ListO[i].y))):
            return False
    return True


"""def deleteRctgl(lPuntos, rectangulos):
    for i in range(len(lPuntos)):
        if(lPuntos[i].prj is not None):
            for j in range(i,len(lPuntos)):
                if(lPuntos[j].prj is not None):
                    if((((lPuntos[i].x<lPuntos[auxj].x and lPuntos[i].prj.x>lPuntos[j].x) and (lpuntos[i].y>lPuntos[j].y and lPuntos[i].prj.y>lPuntos[j].y)) and(lPuntos[i].x<lPuntos[j].prj.x and lPuntos[i].prj.x>lPuntos[j].prj.x) and (lpuntos[i].y<lPuntos[j].prj.y and lPuntos[i].prj.y<lPuntos[j].prj.y))):

                    elif(((lPuntos[i].x>lPuntos[auxj].x and lPuntos[i].prj.x>lPuntos[j].x) and (lpuntos[i].y>lPuntos[j].y and lPuntos[i].prj.y<lPuntos[j].y)) and((lPuntos[i].x<lPuntos[j].prj.x and lPuntos[i].prj.x<lPuntos[j].prj.x) and (lpuntos[i].y>lPuntos[j].prj.y and lPuntos[i].prj.y<lPuntos[j].prj.y))):
"""


def binariSearch(k, l):
    ini = 0
    top = len(l) - 1
    indice = 0
    flag = False
    while ini <= top and not flag:
        md = (ini + top) // 2
        if (l[md].x == k.x):
            flag = True
            indice = md
        else:
            if k.x < l[md].x:
                top = md - 1
            else:
                ini = md + 1
    return indice


def algorithm(lPuntos, aparear):
    dim = 10 ** 1000000
    auxj = 0
    r = 0
    rectangulos = []
    for i in range(len(lPuntos)):
        if (aparear[i] == 0):
            for j in range(i + 1, len(lPuntos)):
                if (aparear[j] == 0):
                    r = binariSearch(lPuntos[i], lPuntos)
                    q = binariSearch(lPuntos[j], lPuntos)
                    if (restriccion(lPuntos[i], lPuntos[j], lPuntos, r, q) and dim > math.sqrt(
                            ((lPuntos[j].x - lPuntos[i].x) ** 2) + ((lPuntos[j].y - lPuntos[i].y) ** 2)) and lPuntos[
                        i].color == lPuntos[j].color):
                        dim = math.sqrt(((lPuntos[j].x - lPuntos[i].x) ** 2) + ((lPuntos[j].y - lPuntos[i].y) ** 2))
                        auxj = j
            if (auxj != 0):
                if (lPuntos[i].std == True and lPuntos[auxj].std == True):
                    rectangulos.append(
                        match.Rectangle(min(lPuntos[i].x, lPuntos[auxj].x), max(lPuntos[i].x, lPuntos[auxj].x),
                                        min(lPuntos[i].y, lPuntos[auxj].y), max(lPuntos[i].y, lPuntos[auxj].y)))
                    aparear[i] = 1
                    aparear[auxj] = 1
                    lPuntos[i].prj = lPuntos[auxj]
                    lPuntos[auxj].prj = lPuntos[i]
                    auxj = 0
                    dim = 10 ** 1000000
            r = 0
            auxj = 0
    return rectangulos


def debugMode():
    pList = []
    rectangulos = []
    pList.append(match.Point(0, 8, 1))
    pList.append(match.Point(1, 5, -1))
    pList.append(match.Point(2, 6, -1))
    pList.append(match.Point(3, 3, 1))
    pList.append(match.Point(4, 9, -1))
    pList.append(match.Point(5, 2, 1))
    pList.append(match.Point(6, 7, 1))
    pList.append(match.Point(8, 1, -1))
    pList.append(match.Point(9, 0, -1))
    lCopy = copy.deepcopy(pList)
    print("Copia de arreglo ordenado")
    showPointList(lCopy)
    aparear = [0] * len(pList)
    rectangulos += algorithm(lCopy, aparear)
    for i in range(len(aparear)):
        print(str(aparear[i]))
    visual.Window(points=pList, rectangles=rectangulos)


aparear(100)