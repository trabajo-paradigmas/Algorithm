from tkinter import *
import math

class Window:
    
    def __init__(self, points=[], rectangles=[]):
        self.root = Tk()
        self.h = 1000
        self.w = 1000
        self.paper = Canvas(self.root,background="white", height=self.h, width=self.w)
        self.center = [0,0]
        self.points = points
        self.boxes = rectangles
        self.zoom = 1.0
        self.t = 3
        self.deltazoom = 0.1
        self.drawnpoints = []
        self.drawnsegments = []
        self.paper.bind("<Button-1>", self.leftclick)
        self.paper.bind("<ButtonRelease-1>", self.release)
        self.paper.bind("<Double-Button-1>", self.doubleclickleft)
        self.paper.bind("<Button-3>",self.rightclick)
        self.paper.bind("<Button-5>",self.zoomout)
        self.paper.bind("<Button-4>",self.zoomin)
        
        self.drawPoints()
        self.paper.pack(fill=BOTH,expand=YES,side=BOTTOM)
        
    def convert_to_screen_coords(self, point):
        x = point[0]-self.center[0]
        y = -(point[1]-self.center[1])
        
        x = x * self.zoom
        y = y * self.zoom
        
        x = x + self.paper.winfo_width()/2
        y = y + self.paper.winfo_height()/2
        
        x = int(x)
        y = int(y)
        
        return [x,y]

    def drawPoints(self):
        
        self.destroyobjects()
        self.centers=[]
        
        grid_segments=[]
        
        x1 = min(self.points, key=lambda p: p.x).x - 1
        x2 = max(self.points, key=lambda p: p.x).x + 1

        y1 = min(self.points, key=lambda p: p.y).y - 1
        y2 = max(self.points, key=lambda p: p.y).y + 1
                
        for i in range(x1,x2+1):
            grid_segments.append([[i,y1],[i,y2]])
            
        for i in range(y1,y2+1):
            grid_segments.append([[x1,i],[x2,i]])
            
        for s in grid_segments:
            p = self.convert_to_screen_coords(s[0])
            q = self.convert_to_screen_coords(s[1])
            self.drawnsegments.append(self.paper.create_line(p[0],p[1],q[0],q[1],fill="light gray"))
            
        for B in self.boxes:
            p = [B.left,B.top]
            q = [B.right,B.bottom]
            p1 = self.convert_to_screen_coords(p)
            q1 = self.convert_to_screen_coords(q)
            self.drawnsegments.append(self.paper.create_line(p1[0],p1[1],q1[0],p1[1],fill="black"))
            self.drawnsegments.append(self.paper.create_line(q1[0],p1[1],q1[0],q1[1],fill="black"))
            self.drawnsegments.append(self.paper.create_line(q1[0],q1[1],p1[0],q1[1],fill="black"))
            self.drawnsegments.append(self.paper.create_line(p1[0],q1[1],p1[0],p1[1],fill="black"))
            
        for p in self.points:
            
            q = self.convert_to_screen_coords([p.x,p.y])
            self.centers.append(q)
            
            x = q[0] - self.t
            y = q[1] - self.t
            
            if p.color==-1:
                self.drawnpoints.append(self.paper.create_oval(x,y,x+2*self.t,y+2*self.t,outline="red",fill="red"))
            elif p.color==1:
                self.drawnpoints.append(self.paper.create_oval(x,y,x+2*self.t,y+2*self.t,outline="blue",fill="blue"))
            elif p.color==2:
                self.drawnpoints.append(self.paper.create_oval(x,y,x+2*self.t,y+2*self.t,outline="green",fill="green"))
        self.root.update()
                
    def moveCenter(self,d):       
        self.center[0]=self.center[0]+(d[0]/self.zoom)
        self.center[1]=self.center[1]+(d[1]/self.zoom)
        
        for p in self.drawnpoints:
            self.paper.move(p,-d[0],d[1])
            
        for s in self.drawnsegments:
            self.paper.move(s,-d[0],d[1])  

    def setzoom(self,zoom):
        self.zoom=zoom
        self.drawPoints()
        
    def destroyobjects(self):
        for p in self.drawnpoints:
            self.paper.delete(p)
        self.drawnpoints=[]
            
        for s in self.drawnsegments:
            self.paper.delete(s)
        self.drawnsegments=[] 
            
    def leftclick(self, event):
        global start
        start=[int(self.paper.canvasx(event.x)),int(self.paper.canvasy(event.y))]
    
    def doublezoomin(self):
        self.setzoom(2*self.zoom)
        
    def doublezoomout(self):
        self.setzoom(self.zoom/2)
        
    def rightclick(self,event):
        self.doublezoomout()
        
    def doubleclickleft(self,event):
        start=[int(self.paper.canvasx(event.x)),int(self.paper.canvasy(event.y))]
        end=[self.paper.winfo_width()/2,self.paper.winfo_height()/2]
        v=[-(end[0]-start[0]),(end[1]-start[1])]
        self.moveCenter([v[0],v[1]])
        self.doublezoomin()
        
    def release(self,event):
        global end
        end=[int(self.paper.canvasx(event.x)),int(self.paper.canvasy(event.y))]
        v=[-(end[0]-start[0]),(end[1]-start[1])]
        self.moveCenter([v[0],v[1]])
    
    def zoomout(self,event):
        if self.zoom >= 1.0:
            self.setzoom(self.zoom-self.deltazoom)
        else:
            zoominv=1/self.zoom
            newzoominv=zoominv+self.deltazoom*zoominv
            self.setzoom(1/(newzoominv))
                
    def zoomin(self,event):
        if self.zoom >= 1.0:
            self.setzoom(self.zoom+self.deltazoom*self.zoom)
        else:
            zoominv=1/self.zoom
            newzoominv=zoominv-self.deltazoom*zoominv
            self.setzoom(1/(newzoominv))
            
    def take_picture(self,filename=None):
        if filename == None:
            filename=asksaveasfilename(filetypes=[("postscript","*.ps *.eps")],defaultextension=".ps")
        self.paper.postscript(file=filename)
        
