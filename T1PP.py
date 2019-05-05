import match
import math
import deepcopy from copy

def aparear(n):
	P = match.create_random_points(n)
	xr = yr = 0
	xa = ya=0
	grpR=[]
	grpA=[]
	P=mergeList(P)
	for i in range(len(P)):
		if(P[i].color==-1):
			grpR[i]=P.deepcopy(i)
		else:
			grpA[i]=P.deepcopy(i)
	R=heuristic(P)
	algorithm(grpR, grpA)
	return 2 * len(R) / 2

def heuristic(P):
	showlistPoint(P)

def algorithm(lPuntos, lRestriccion):
	L=[] #Correspondiente a la lista de rectangulos obtenidos
	dim=0
	aux=0
	yaux = 0
	xaux = 0
	for i in range(len(lPuntos)):
		for j in range(i+1, len(lPuntos)):
			if(dim<math.sqrt(((lPuntos[j].x-lPuntos[i].x)**2)+((lPuntos[j].y-lPuntos[i].y)**2))):
				dim=math.sqrt(((lPuntos[j].x-lPuntos[i].x)**2)+((lPuntos[j].y-lPuntos[i].y)**2))
				aux=j
		if(L[0] == None):
			yaux[] = [lPuntos[i].y,lPuntos[j].y]
			xaux[] = [lPuntos[i].x,lPuntos[j].x]
		else:
			if lPuntos[i].x < lPuntos[j].x:

# def dijkstra(D):		Estoy repensando esto del Dijkstra, quizas con solo ordenar sea suficiente
# 	Para ello pienso que se puede crear una nueva lista de pares ordenados de pares ordenados Rec(P1,P2)
# 	esto es porque me di cuenta de que cada punto no puede tener otro en el mismo eje x o y POR DEFINICION DEL PROBLEMA

	return D
def mergeList(A): #Avance 02/05, falta mota jaja
	if len(A) >1:
	md=len(arr)//2
	l=A[:md]
	r=A[mid:]
	mergeList(l)
	mergeList(r)
	i=j=k=0
	c=[]
	while i<len(l) and j<len(r):
		if(l[i].x<=r[j].x):
			c.append(A[i])
			i+=1
		else:
			c.append(B[j])
			j+=1
	while i<len(A):
		c.append(A[i])
		i+=1
	while j<len(B):
		c.append(B[i])
		j+=1
	return c
def showlistPoint(P):
	for i in range(P):
		print("("+str(i.x)+", "+str(i.y)+", "+str(i.color)+")")

aparear(5)