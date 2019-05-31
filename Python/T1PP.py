import match
import visual
import math
import copy
import time


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
    visual.Window(points=Px, rectangles=rectangulos)


def not_in_R(Rec, P1, P2):
    for i in range(len(Rec)):
        if ((Rec[i].left < min(P1.x, P2.x) and Rec[i].right > max(P1.x, P2.x)) or (
                Rec[i].bottom < min(P1.y, P2.y) and Rec[i].top > max(P1.y, P2.y))):
            return False
    return True


def restriccion(A, B, list, p, q, rect):
    if(p < 0):
        p = 0
    if(q == len(list)):
        q = q - 1
    for i in range(p, q + 1):
        x = int(list[i].x)
        y = int(list[i].y)
        if (A.color != B.color):
            return False
        if(list[i].x > min(A.x, B.x)):
            if(list[i].x < max(A.x, B.x)):
                if(list[i].y > min(A.y, B.y)):
                    if(list[i].y < min(A.y, B.y)):
                        return False
    return not_in_R(rect, A, B)

def distanceFuntion(P1, P2):
    return math.sqrt(((P2.x - P1.x) ** 2) + ((P2.y - P1.y) ** 2))


def binariSearch(k, l):
    ini = 0
    top = len(l) - 1
    indice = -1
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

def next_point(indice, lista, op = 1):
    k = indice + op

    while((lista[indice].color != lista[k].color) and (k >= len(lista) or k < 0)):
        k = k + op
    return k

def algorithm(XPuntos, YPuntos):
    rectangulos = []
    xs = -1
    xr = -1
    ys = -1
    yr = -1
    dim = 10 ** 1000000
    for i in range(len(YPuntos)):
        if (i == 0):
            x = binariSearch(YPuntos[i], XPuntos)
            if (x == 0):
                xs = next_point(x, XPuntos)
                ys = next_point(i, YPuntos)
            elif (x == (len(XPuntos) - 1)):
                xr = next_point(x, XPuntos, -1)
                ys = next_point(i, YPuntos)
            else:
                xs = next_point(x, XPuntos)
                xr = next_point(x, XPuntos, -1)
                ys = next_point(i, YPuntos)
        elif (i == (len(YPuntos) - 1)):
            x = binariSearch(YPuntos[i], XPuntos)
            if (x == 0):
                xs = next_point(x, XPuntos)
                yr = next_point(i, YPuntos, -1)
            elif (x == (len(XPuntos) - 1)):
                xr = next_point(x, XPuntos, -1)
                yr = next_point(i, YPuntos, -1)
            else:
                xs = next_point(x, XPuntos)
                xr = next_point(x, XPuntos, -1)
                yr = next_point(i, YPuntos, -1)
        else:
            x = binariSearch(YPuntos[i], XPuntos)
            if (x == 0):
                xs = next_point(x, XPuntos)
                ys = next_point(i, YPuntos)
                yr = next_point(i, YPuntos, -1)
            elif (x == (len(XPuntos) - 1)):
                xr = next_point(x, XPuntos, -1)
                yr = next_point(i, YPuntos, -1)
                ys = next_point(i, YPuntos)
            else:
                xs = next_point(x, XPuntos)
                xr = next_point(x, XPuntos, -1)
                yr = next_point(i, YPuntos, -1)
                ys = next_point(i, YPuntos)
        punto = match.Point(0,0,0)
        aux = [xs, xr, ys, yr]
        for e in aux:
            if(e == xs or e == xr):
                aux1 = distanceFuntion(YPuntos[i], XPuntos[e])
                if ((dim > aux1) and ((restriccion(YPuntos[i], XPuntos[e], YPuntos, i - 1, i + 1, rectangulos) == False) and (
                        restriccion(YPuntos[i], XPuntos[e], XPuntos, x - 1, x + 1, rectangulos) == False))):
                    dim = aux1
                    punto = XPuntos[e]
            else:
                aux1 = distanceFuntion(YPuntos[i], XPuntos[e])
                if ((dim > aux1) and ((restriccion(YPuntos[i], YPuntos[e], YPuntos, i - 1, i + 1, rectangulos) == False) and (
                        restriccion(YPuntos[i], YPuntos[e], XPuntos, x - 1, x + 1, rectangulos) == False))):
                    dim = aux1
                    punto = YPuntos[e]

        if (punto.x != 0 and punto.y != 0):
            r = match.Rectangle(min(YPuntos[x].x, punto.x), max(YPuntos[x].x, punto.x), min(YPuntos[x].y, punto.y),
                                max(YPuntos[x].y, punto.y))
            rectangulos.append(r)
    return rectangulos


aparear(100)
