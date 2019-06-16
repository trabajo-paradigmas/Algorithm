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
    rectangulos += algorithm(Px, Py)
    porcentaje = (len(rectangulos) * 2 * 100) / len(Px)
    ejecucion = time.time() - tiempo
    print("El procentaje de apareamiento de puntos fue de: {}".format(porcentaje))
    print("El timepo de ejecucion fue de: {}".format(ejecucion))
    visual.Window("El procentaje de apareamiento de puntos fue de: {}".format(porcentaje), points=Px,
                  rectangles=rectangulos)
    input("Pause...")


def not_in_R(Rec, P1, P2):
    for i in range(len(Rec, -1):
        if
    (Rec[i].right < P1.x):
    return True
    elif (((P1.x > Rec[i].right) and (P2.x > Rec[i].left)) or ((P1.y < Rec[i].bottom) and (P2.y < Rec[i].bottom)) or (
                (P1.y > Rec[i].bottom) and (P2.y > Rec[i].bottom)))):
    return True
    elif (((P1.x > Rec[i].right) and (P1.y < Rec[i].bottom)) and ((P2.x > Rec[i].right) and (P1.y < Rec[i].bottom))):


def algorithm(Puntos):
    rectangulos = []
    for i in range(len(Puntos) - 1):
        rest_y_arr = -1
        rest_x = -1
        rest_y_abj = -1
        if ((i + 1) < len(Puntos)):
            j = i + 1
            while ((abs(rest_y_arr - rest_y_abj)) != 1):
                if Puntos[i].color == Puntos[j].color:
                    if not_in_R(rectangulos, Puntos[i], Puntos[j]):
                        r = match.Rectangle(min(Puntos[i].x, Puntos[j].x), max(Puntos[i].x, Puntos[j].x),
                                            min(Puntos[i].y, Puntos[j].y), max(Puntos[i].y, Puntos[j].y))
                        rectangulos.append(r)
                        break
                elif (Puntos[j].y < Puntos[i].y or (rest_y_abj < Puntos[j].y)):
                    rest_y_abj = Puntos[j].y
                elif (Puntos[j].y > Puntos[i].y or (rest_y_arr > Puntos[j].y)):
                    rest_y_arr = Puntos[j].y
    return rectangulos


aparear(100)
