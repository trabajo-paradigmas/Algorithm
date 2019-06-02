import copy
import math
import time

import match
import visual


def showPointList(l):
    for i in range(len(l)):
        print("(" + str(l[i].x) + ", " + str(l[i].y) + ", " + str(l[i].color) + ")")


def aparear(n):
    tiempo = time.time()
    Px = match.create_random_points(n)
    rectangulos = []
    Px.sort(key=lambda Point: Point.x)
    Py = copy.deepcopy(Px)
    Py.sort(key=lambda Point: Point.y)
    rectangulos += algorithm(Px, Py)
    porcentaje = (len(rectangulos) * 2 * 100) / len(Px)
    ejecucion = time.time() - tiempo
    print("El procentaje de apareamiento de puntos fue de: {}".format(porcentaje))
    print("El timepo de ejecucion fue de: {}".format(ejecucion))
    visual.Window("El procentaje de apareamiento de puntos fue de: {}".format(porcentaje), points=Px,
                  rectangles=rectangulos)
    input("Pause...")


def not_in_R(Rec, P1, P2):
    if len(Rec) == 0:
        return True
    for i in range(len(Rec)):
        if ((Rec[i].left < min(P1.x, P2.x) and Rec[i].right > max(P1.x, P2.x)) and (
                Rec[i].bottom < min(P1.y, P2.y) and Rec[i].top > max(P1.y, P2.y))):
            return False
    return True


def restriccion(A, B, ListO, p, q):
    for i in range(p, q):
        x = int(ListO[i].x)
        y = int(ListO[i].y)
        if (A.std == True or B.std == True):
            return False
        if (A.color != B.color):
            return False
        if ((x > min(A.x, B.x) and x < max(A.x, B.x)) or (y > min(A.y, B.y) and y < max(A.y, B.y))):
            return False
    return True


def distanceFuntion(P1, P2):
    return math.sqrt(((P2.x - P1.x) ** 2) + ((P2.y - P1.y) ** 2))


def binariSearch(k, l):
    ini = 0
    top = len(l) - 1
    indice = -1
    flag = False
    while ini <= top and not flag:
        md = (ini + top) // 2
        if l[md].x == k.x:
            flag = True
            indice = md
        else:
            if k.x < l[md].x:
                top = md - 1
            else:
                ini = md + 1
    return indice


def next_point(indice, lista, op=1):
    k = indice + op

    while (lista[indice].color != lista[k].color) and (k >= len(lista) or k < 0):
        k = k + op
    return k


def algorithm(XPuntos, YPuntos):
    rectangulos = []
    xs = 0
    xr = 0
    ys = 0
    yr = 0
    dim = 10 ** 1000000
    for i in range(len(YPuntos)):
        if i == 0:
            x = binariSearch(YPuntos[i], XPuntos)
            if x == 0:
                xs = next_point(x, XPuntos)
                ys = next_point(i, YPuntos)
            elif x == (len(XPuntos) - 1):
                xr = next_point(x, XPuntos, -1)
                ys = next_point(i, YPuntos)
            else:
                xs = next_point(x, XPuntos)
                xr = next_point(x, XPuntos, -1)
                ys = next_point(i, YPuntos)
        elif i == (len(YPuntos) - 1):
            x = binariSearch(YPuntos[i], XPuntos)
            if x == 0:
                xs = next_point(x, XPuntos)
                yr = next_point(i, YPuntos, -1)
            elif x == (len(XPuntos) - 1):
                xr = next_point(x, XPuntos, -1)
                yr = next_point(i, YPuntos, -1)
            else:
                xs = next_point(x, XPuntos)
                xr = next_point(x, XPuntos, -1)
                yr = next_point(i, YPuntos, -1)
        else:
            x = binariSearch(YPuntos[i], XPuntos)
            if x == 0:
                xs = next_point(x, XPuntos)
                ys = next_point(i, YPuntos)
                yr = next_point(i, YPuntos, -1)
            elif x == (len(XPuntos) - 1):
                xr = next_point(x, XPuntos, -1)
                yr = next_point(i, YPuntos, -1)
                ys = next_point(i, YPuntos)
            else:
                xs = next_point(x, XPuntos)
                xr = next_point(x, XPuntos, -1)
                yr = next_point(i, YPuntos, -1)
                ys = next_point(i, YPuntos)
        punto = [0, 0]
        aux = [xs, xr, ys, yr]
        aux1 = 10 ** 1000000
        for e in aux:
            if e == xs or e == xr:
                aux1 = distanceFuntion(YPuntos[i], XPuntos[e])
                if ((dim > aux1) and ((restriccion(YPuntos[i], XPuntos[e], YPuntos, i - 1, i + 1) != False) and (
                        restriccion(YPuntos[i], XPuntos[e], XPuntos, x - 1, x + 1) != False))):
                    dim = aux1
                    punto = [e, 1]
            elif e == ys or e == yr:
                aux1 = distanceFuntion(YPuntos[i], YPuntos[e])
                if ((dim > aux1) and ((restriccion(YPuntos[i], YPuntos[e], YPuntos, i - 1, i + 1) == True) and (
                        restriccion(YPuntos[i], YPuntos[e], YPuntos, x - 1, x + 1) == True))):
                    dim = aux1
                    punto = [e, -1]
        p1 = punto[0]
        p2 = punto[1]
        if (p2 == 1) and (not_in_R(rectangulos, YPuntos[i], YPuntos[p1]) == True):
            r = match.Rectangle(min(YPuntos[x].x, YPuntos[p1].x), max(YPuntos[x].x, YPuntos[p1].x),
                                min(YPuntos[x].y, YPuntos[p1].y),
                                max(YPuntos[x].y, YPuntos[p1].y))
            YPuntos[i].std = True
            YPuntos[p1].std = True
            print("Agregando...")
            rectangulos.append(r)
        elif (not_in_R(rectangulos, YPuntos[i], XPuntos[p1]) == True):
            r = match.Rectangle(min(YPuntos[x].x, XPuntos[p1].x), max(YPuntos[x].x, XPuntos[p1].x),
                                min(YPuntos[x].y, XPuntos[p1].y),
                                max(YPuntos[x].y, XPuntos[p1].y))
            YPuntos[i].std = True
            XPuntos[p1].std = True
            print("Agregando...")
            rectangulos.append(r)
    return rectangulos


aparear(100)
