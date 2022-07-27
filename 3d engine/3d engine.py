from tkinter import *
root=Tk()
root.title("wave eq")
root.geometry("700x500")
graph=Canvas(root,width=300,height=200,bg="green")
graph.pack(fill="both",expand=True)

#only draw sides you can see by looking at 2d map of vertices

#box centered at .5,.5,.5 with sL=1
x=[0,1,0,1,0,1,0,1]
y=[0,0,0,0,1,1,1,1]
z=[0,0,1,1,0,0,1,1]

#observation at x=.5,y=-2, z=.5
#move observation

#4-->6
scale=2000
xoff=-1950
yoff=-1950

print(scale*x[4]+xoff,scale*y[4]+yoff,scale*x[6]+xoff,scale*y[6]+yoff)
graph.create_line(scale*x[4]+xoff,scale*y[4]+yoff,scale*x[6]+xoff,scale*y[6]+yoff,fill="blue",width=2)

for i in range(len(x)):
    for j in range(len(x)):
        #print(scale*x[i]+xoff,scale*y[j]+yoff,scale*x[i]+xoff,scale*y[j]+yoff)
        graph.create_line(scale*x[i]+xoff,scale*y[j]+yoff,scale*x[i]+xoff,scale*y[j]+yoff,fill="blue",width=2)
#graph.create_line(150,10,200,0,fill="blue",width=2)

#graph.create_line(300,500,200,200,fill="blue",width=2)

parallax=.1
p=parallax

#parallax y to x gets distorted by total distance and distance x
#parallax brings distant points to center of view



obx=3
oby=2
obz=4


for i in range(len(x)):
    d=((obx-x[i])**2+(oby-y[i])**2+(obz-z[i])**2)**.5
    dyz=((oby-y[i])**2+(obz-z[i])**2)**.5
    dxz=((oby-y[i])**2+(obz-z[i])**2)**.5
    dx=(obx-x[i])
    dy=(oby-y[i])
    
    x[i]+=dx/(dyz**p)
    y[i]+=dy/(dxz**p)
    
    """dy=(oby-y[i])/d
    y[i]+=dy*(p*d)
    dz=(obz-z[i])/d
    z[i]+=dz*(p*d)"""

scale=1000#2000
xoff=-2500
yoff=-1600
graph.create_line(scale*x[4]+xoff,scale*y[4]+yoff,scale*x[6]+xoff,scale*y[6]+yoff,fill="blue",width=2)
for i in range(len(x)):
    for j in range(len(x)):
            graph.create_line(scale*x[i]+xoff,scale*y[i]+yoff,scale*x[j]+xoff,scale*y[j]+yoff,fill="blue",width=2)

            
print(scale*x[4]+xoff,scale*y[4]+yoff,scale*x[6]+xoff,scale*y[6]+yoff)













