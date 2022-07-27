from tkinter import *
import keyboard
root=Tk()
root.title("wave eq")
root.geometry("1920x1080")
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
"""
for i in range(len(x)):
    for j in range(len(x)):
        #print(scale*x[i]+xoff,scale*y[j]+yoff,scale*x[i]+xoff,scale*y[j]+yoff)
        graph.create_line(scale*x[i]+xoff,scale*y[j]+yoff,scale*x[i]+xoff,scale*y[j]+yoff,fill="blue",width=2)
#graph.create_line(150,10,200,0,fill="blue",width=2)
"""
#graph.create_line(300,500,200,200,fill="blue",width=2)

parallax=1.414
p=parallax

#parallax y to x gets distorted by total distance and distance x
#parallax brings distant points to center of view



obx=.5
oby=.5
obz=3

speed=.002

tilt=0

b=0
while True:
    b+=1
    xog=[]
    yog=[]
    zog=[]
    for i in range(len(x)):
        xog.append(x[i])
        yog.append(y[i])
        zog.append(z[i])
    for i in range(len(x)):
        d=((obx-x[i])**2+(oby-y[i])**2+(obz-z[i])**2)**.5
        dyz=((oby-y[i])**2+(obz-z[i])**2)**.5
        dxz=((obx-x[i])**2+(obz-z[i])**2)**.5
        dxy=((obx-x[i])**2+(oby-y[i])**2)**.5
        dx=(obx-x[i])
        dy=(oby-y[i])
        dz=(obz-z[i])
                
        
        xog[i]+=dx+dx*p**(-dyz)
        yog[i]+=dy+dy*p**(-dxz)

        #xog[i]+=tilt*dz*.01

        
        
    if keyboard.is_pressed('up arrow'):
        oby-=speed
    if keyboard.is_pressed('down arrow'):
        oby+=speed
    if keyboard.is_pressed('right arrow'):
        obx+=speed
    if keyboard.is_pressed('left arrow'):
        obx-=speed
    if keyboard.is_pressed('p'):
        print(scale*xog[i]+xoff,scale*yog[i]+yoff,scale*xog[j]+xoff,scale*yog[j]+yoff)
    if keyboard.is_pressed('w'):
        obz+=speed*2
    if keyboard.is_pressed('s'):
        obz-=speed*2

    if keyboard.is_pressed('a'):
        tilt+=.001

            
    if keyboard.is_pressed('d'):
        tilt-=.001
        
    for i in range(len(x)):
        xog[i]+=tilt
    
    print(xog[i])  
    scale=1500


    xoff=000
    yoff=0
    
    #graph.create_line(scale*x[4]+xoff,scale*y[4]+yoff,scale*x[6]+xoff,scale*y[6]+yoff,fill="blue",width=2)
    for i in range(len(x)):
        for j in range(len(x)):
                graph.create_line(scale*xog[i]+xoff,scale*yog[i]+yoff,scale*xog[j]+xoff,scale*yog[j]+yoff,fill="blue",width=2)
                #print(scale*xog[i]+xoff,scale*yog[i]+yoff,scale*xog[j]+xoff,scale*yog[j]+yoff) 
    #print(scale*xog[i]+xoff,scale*yog[i]+yoff,scale*xog[j]+xoff,scale*yog[j]+yoff)      
    #print(scale*x[4]+xoff,scale*y[4]+yoff,scale*x[6]+xoff,scale*y[6]+yoff)
    root.update()
    if j%2:
        graph.delete('all')












