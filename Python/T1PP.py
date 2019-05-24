import match
import visual
import copy
import math
from time import time
from  functools import  reduce


def aparear(n):
    P = match.create_random_points(n)
    pAx = []
    pAy = []
    pRx = []
    pRy = []
    P.sort(key=lambda Point: Point.x)
    for i in range(len(P)):
        if (P[i].color == -1):
            pAx.append(copy.deepcopy(P[i]))
        else:
            pRx.append(copy.deepcopy(P[i]))
    pRy = copy.deepcopy(pRx)
    pRy.sort(key=lambda Point: Point.y)
    pAy = copy.deepcopy(pAx)
    pAy.sort(key=lambda Point: Point.y)
    heuristica(pRx, pRy, pAx, pAy, P)


def p_en_P(p, L, k = 0):
    if k < 0:
        k = 0
    while (p.x == L[k].x and k < len(L)):
        k += 1
    return k


def No_rectang(p1, p2, R):  # p1 = punto menor ; p2 = punto mayor ; R = Lista de rectángulos ya formados
    for i in R:
        if ((i.left <= p1.x and i.right >= p1.x) or (i.left <= p2.x and i.right >= p2.x)) or (
                (i.bottom <= p1.y and i.top >= p1.y) or (i.bottom <= p2.y and i.top >= p2.y)):
            return False
    return True


def restriccion(A, B, ListO, p,
                q):  # A = punto menor   ;   B = punto mayor   ;   List0 = Lista total de puntos ordenados en x    ;   p y q = rango en x del arreglo total de A y B
    for i in range(p, q + 1):
        x = int(ListO[i].x)
        y = int(ListO[i].y)
        if ((x >= min(A.x, B.x) and x <= max(A.x, B.x)) or (y >= min(A.y, B.y) and y <= max(A.y, B.y))):
            return False
    return True




def distanceFuntion(P1, P2):
    return math.sqrt(((P2.x - P1.x) ** 2) + ((P2.y - P1.y) ** 2))


def comp_par(P, pivote, Px, Py, pivx, x_en_y, rectangulo):
    if distanceFuntion(Px[pivx],Px[pivx-1]) == reduce(min,(distanceFuntion(Px[pivx],Px[x_en_y + 1]), distanceFuntion(Px[pivx],Py[x_en_y-1]), distanceFuntion(Px[pivx],Px[pivx+1])), distanceFuntion(Px[pivx],Px[pivx-1])):
        if restriccion(Px[pivx], P[p_en_P(Px[pivx-1], P)],P, pivote, p_en_P(Px[pivx-1], P)) and No_rectang(Px[pivx], P[p_en_P(Px[pivx-1])],rectangulo):
            return int( p_en_P(Px[pivx-1], P))
    elif distanceFuntion(Px[pivx],Px[pivx+1]) == reduce(min,(distanceFuntion(Px[pivx],Px[x_en_y + 1]), distanceFuntion(Px[pivx],Py[x_en_y-1]), distanceFuntion(Px[pivx],Px[pivx+1])), distanceFuntion(Px[pivx],Px[pivx-1])):
        if restriccion(Px[pivx], P[p_en_P(Px[pivx + 1], P)], P, pivote, p_en_P(Px[pivx + 1], P)) and No_rectang(Px[pivx], P[p_en_P(Px[pivx+1])],rectangulo):
            return int(p_en_P(Px[pivx + 1], P))
    elif distanceFuntion(Px[pivx],Py[x_en_y-1]) == reduce(min,(distanceFuntion(Px[pivx],Px[x_en_y + 1]), distanceFuntion(Px[pivx],Py[x_en_y-1]), distanceFuntion(Px[pivx],Px[pivx+1])), distanceFuntion(Px[pivx],Px[pivx-1])):
        if restriccion(Px[pivx], P[p_en_P(Py[x_en_y - 1], P)], P, pivote, p_en_P(Py[x_en_y - 1], P)) and No_rectang(Px[pivx], P[p_en_P(Py[x_en_y-1])],rectangulo):
            return int(p_en_P(Py[x_en_y - 1], P))
    elif distanceFuntion(Px[pivx],Py[x_en_y+1]) == reduce(min,(distanceFuntion(Px[pivx],Px[x_en_y + 1]), distanceFuntion(Px[pivx],Py[x_en_y-1]), distanceFuntion(Px[pivx],Px[pivx+1])), distanceFuntion(Px[pivx],Px[pivx-1])):
        if restriccion(Px[pivx], P[p_en_P(Py[x_en_y + 1], P)], P, pivote, p_en_P(Py[x_en_y + 1], P)) and No_rectang(Px[pivx], P[p_en_P(Py[x_en_y+1])],rectangulo):
            return int(p_en_P(Py[x_en_y + 1], P))
    else:
        return -1

def algorthm(Px, Py, P, rectangulos):
    auxX = p_en_P(Px[1], P, 0)
    auxY = p_en_P(Px[1], Py, 0)
    yAx = p_en_P(Py[auxY], P, 0)
    for k in range(1, len(Px)-2):
        auxX = p_en_P(Px[k], P, auxX)
        auxY = p_en_P(Px[k], Py, auxY)
        yAx = p_en_P(Py[auxY], P, yAx)
        j = comp_par(P, auxX, Px, Py, k, yAx, rectangulos)
        if j != -1:
            rectangulos.append(match.Rectangle(min(P[k].x, P[j].x), max(P[k].x, P[j].x), min(P[k].y, P[j].y), max(P[k].y, P[j].y)))


def heuristica(pRx, pRy, pAx, pAy, P):
    tiempo = time()
    rectangulos = []
    marc = [0] * len(P)
    algorthm(pRx, pRy, P, rectangulos)
    algorthm(pAx, pAy, P, rectangulos)
    porcentaje = (len(rectangulos) * 2 * 100) / len(P)
    ejecucion = time() - tiempo
    print("El procentaje de apareamiento de puntos fue de: {}".format(porcentaje))
    print("El timepo de ejecucion fue de: {}".format(ejecucion))
    visual.Window(points=P, rectangles=rectangulos)


aparear(100)
