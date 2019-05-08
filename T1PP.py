import match
import visual
import math
import copy

def showPointList(l):
    for i in range(len(l)):
        print("("+str(l[i].x)+", "+str(l[i].y)+", "+str(l[i].color)+")")

def aparear(n):
    P = match.create_random_points(n)
    rectangulos=[]
    showPointList(P)
    aparear=[0]*len(P)
    P.sort(key=lambda Point: Point.x)
    print("Arreglo ordenado")
    showPointList(P)
    lCopy=copy.deepcopy(P)
    print("Copia de arreglo ordenado")
    showPointList(lCopy)
    for i in range(int(math.sqrt(n))+1): #Se ejecutará (n)^1/2 veces el algoritmo
        rectangulos+=algorithm(lCopy, lCopy, aparear)
    for i in range(len(aparear)):
        print(str(aparear[i]))
    visual.Window(points=P,rectangles=rectangulos) 
def restriccion(A, B, ListO, p, q):
    for i in range(p, q):
        if((A.x<ListO[i].x and A.y<ListO[i].x and B.x>ListO[i].x and B.y>ListO[i].y) or (A.x>ListO[i].x and A.y>ListO[i].x and B.x<ListO[i].x and B.y<ListO[i].y)):
            return False
    return True
def binariSearch(k, l):
    ini=0
    top=len(l)-1
    indice=0
    flag = False
    while ini<=top and not flag:
        md=(ini+top)//2
        if(l[md].x==k.x):
            flag=True
            indice=md
        else:
            if k.x<l[md].x:
                top=md-1
            else:
                ini=md+1
    return indice

def algorithm(lPuntos, lRestriccion, aparear):
    dim=10**1000000
    auxj=0
    r=0
    rectangulos=[]
    for i in range(len(lPuntos)):
        if(aparear[i]==0):
            for j in range(i+1, len(lPuntos)):
                if(aparear[j]==0):
                    r=binariSearch(lPuntos[i], lRestriccion)
                    if(dim>math.sqrt(((lPuntos[j].x-lPuntos[i].x)**2)+((lPuntos[j].y-lPuntos[i].y)**2)) and restriccion(lPuntos[i], lPuntos[j], lRestriccion, r, j) and lPuntos[i].color==lPuntos[j].color):
                        dim=math.sqrt(((lPuntos[j].x-lPuntos[i].x)**2)+((lPuntos[j].y-lPuntos[i].y)**2))
                        auxj=j
            if(auxj!=0):
                rectangulos.append(match.Rectangle(min(lPuntos[i].x,lPuntos[auxj].x), max(lPuntos[i].x,lPuntos[auxj].x), min(lPuntos[i].y,lPuntos[auxj].y), max(lPuntos[i].y,lPuntos[auxj].y)))
                aparear[i]=1
                aparear[auxj]=1
                auxj=0
            r=0
    return rectangulos
aparear(1000)
