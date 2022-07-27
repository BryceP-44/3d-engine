from math import *
from tkinter import *
import keyboard
root=Tk()
root.title("wave eq")
root.geometry("1920x1080")
graph=Canvas(root,width=300,height=200,bg="green")
graph.pack(fill="both",expand=True)

t=0
info=[[sin(t),cos(t),sin(t+1.57)],[sin(t),cos(t),sin(t+1.57)]]
lines=[[0,1],[2,3],[4,5],[6,7]]
proj=[]
for i in range(len(info)):
    proj.append([0,0])

obsx=0
obsy=0
obsz=-2
betax=0
betaz=0
theta=120*pi/180
tot=tan(theta)

speed=.01
scale=1000
off=200 
dd=10**-200

yes=0
cont=1
while cont==1:
    t+=.002
    info=[[3*sin(t+.57),3*sin(t),3*cos(t)],[0,0,0]]
    yes+=1
    for i in range(len(info)):
        #y
        use=info[i]
        dz=obsz-use[2]
        #print((obsy-use[1])**2+(obsz-use[2])**2)
        ryz=((obsy-use[1])**2+(obsz-use[2])**2)**.5
        dxz=((obsx-use[0])**2+(obsz-use[2])**2)**.5
        #print(dz,ryz)
        #print(dz/ryz)
        phi1=acos(dz/(ryz+dd))
        phi2=phi1+(pi/2)
        dy=obsy-use[1]
        #print(ryz*sin(phi1),dy)
        if ryz*sin(phi1)-dy<.000001:
            phix=phi1
        if ryz*sin(phi2)-dy<.000001:
            phix=phi2
        
        #if phix-betax>=theta and phix-betax<=180-theta:
        yp=(use[1]-obsy)/(2*dxz)*tot+.5#(ryz*cos(phix-betax)-obsy)/(2*dxz)*tan(theta)+.5
        #print(yp)
        proj[i][1]=yp

        #x
        rxz=((obsx-use[0])**2+(obsz-use[2])**2)**.5
        dyz=((obsy-use[1])**2+(obsz-use[2])**2)**.5
        phi1=asin(dz/rxz)
        phi2=phi1+(pi/2)
        dy=obsy-use[1]
        dx=obsx-use[0]
        #print(rxz)
        #print(phi2)
        if rxz*cos(phi1)-dx<.000001:
            phiz=phi1
        if rxz*cos(phi2)-dx<.000001:
            phiz=phi2
        #if phiz-betaz>=theta and phiz-betaz<=180-theta:
        #print("HELO")
        xp=(use[0]-obsx)/(2*dyz+dd)*tot+.5#(rxz*cos(phiz-betaz)-obsx)/(2*dyz+dd)*tan(theta)+.5
        #print(xp)
        proj[i][0]=xp

    #print(proj)
    for i in range(len(proj)):
        for j in range(len(proj)):
            if i!=j:
                p1x=proj[i][0]
                p1y=proj[i][1]
                p2x=proj[j][0]
                p2y=proj[j][1]
                graph.create_line(scale*p1x+off,scale*p1y+off,scale*p2x+off,scale*p2y+off,width=20)
                #print(scale*p1x+off,scale*p1y+off,scale*p2x+off,scale*p2y+off)
    """for i in range(len(lines)):
        ninja=lines[i]
        p1=proj[ninja[0]]
        p1x=p1[0]
        p1y=p1[1]
        p2=proj[ninja[1]]
        p2x=p2[0]
        p2y=p1[1]
        graph.create_line(scale*p1x+off,scale*p1y+off,scale*p2x+off,scale*p2y+off,width=5)
        #print(scale*p1x+50,scale*p1y+50,scale*p2x+50,scale*p2y+50)"""
        
    #graph.create_line(scale*proj[0][0]+50,scale*proj[0][1]+50,scale*proj[1][0]+50,scale*proj[1][1]+50,width=5)
    root.update()
    graph.delete('all')
    #print("hello")
    if keyboard.is_pressed('up arrow'):
        obsy+=speed
    if keyboard.is_pressed('down arrow'):
        obsy-=speed
    if keyboard.is_pressed('right arrow'):
        obsx+=speed
    if keyboard.is_pressed('left arrow'):
        obsx-=speed
    if keyboard.is_pressed('w'):
        obsz+=speed
    if keyboard.is_pressed('s'):
        obsz-=speed
    if keyboard.is_pressed('a'):
        betaz+=speed
    if keyboard.is_pressed('d'):
        betaz-=speed
