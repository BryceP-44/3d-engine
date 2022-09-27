from convert3 import *
from math import *
import keyboard
import random
import cv2
import numpy as np
import time



img = np.zeros((1080,1920,3), np.uint8)



theta=80*pi/180
obsx=0
obsy=0
obsz=-20
betax=0
speed=10
coords=[]
dd=10**-200
dt=.001
gc=5
scale=10
size=50
offx=0
offy=0
b=[]
vx=[]
vy=[]
vz=[]
m=[]

#for i in range
for i in range(100):
    coords.append([random.randint(-10,10),random.randint(-10,10),random.randint(-10,10)])
    #coords=[[10,10,10],[10,-20,10],[20,-15,10],[-15,20,-10]]
    b.append([0,0])
    #b=[[0,0],[0,0],[0,0],[0,0]]
    vx.append(random.randint(-100,100))
    vy.append(random.randint(-100,100))
    vz.append(random.randint(-100,100))
    m.append(random.randint(2,10))

m[len(coords)-4]=5000

scale=1000
off=100


while True:
    ti=time.time()
    #gravity function gravity(coords)
    for i in range(len(coords)): #focus
        ax=0
        ay=0
        az=0
        dax=0
        day=0
        daz=0

        obj1=coords[i]
        x1,y1,z1=obj1[0],obj1[1],obj1[2]

        for j in range(len(coords)):
            #if i!=j:
                obj2=coords[j]

                x2,y2,z2=obj2[0],obj2[1],obj2[2]
                r=((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)**.5
                rx=x2-x1
                ry=y2-y1
                rz=z2-z1
                dax+=(gc*m[j]*rx)/(r**3+dd) #-1*vx[i]**1
                day+=(gc*m[j]*ry)/(r**3+dd) #-1*vy[i]**1
                daz+=(gc*m[j]*rz)/(r**3+dd) #-1*vz[i]**1

                        
                ax=dax
                ay=day
                az=daz
                vx[i]+=ax*dt

                vy[i]+=ay*dt
                vz[i]+=az*dt
                
                if -size>coords[i][0] or coords[i][0]>size:
                    #print("hello")
                    if vx[i]>0:
                        coords[i][0]=500
                    else:
                        coords[i][0]=-500
                    vx[i]*=-1
                    
                if -size>coords[i][1] or coords[i][1]>size:
                    if vy[i]>0:
                        coords[i][1]=500
                    else:
                        coords[i][1]=-500
                    vy[i]*=-1
                if -size>coords[i][2] or coords[i][2]>size:
                    if vz[i]>0:
                        coords[i][2]=500
                    else:
                        coords[i][2]=-500
                    vz[i]*=-1
                    
                b[i]=[x1+vx[i]*dt,y1+vy[i]*dt,z1+vz[i]*dt]


    for i in range(len(b)):
        coords[i]=b[i]

                

    #convert 3d to 2d and draw circles
    a=convert(coords,theta,obsx,obsy,obsz,betax)
    #print(a)
    img = np.zeros((1080,1920,3), np.uint8)
    for i in range(len(a)):
        use=a[i]

        x=use[0]*1920
        y=use[1]*1080

        
        center=(round(x)+offx,round(y)+offy)
        #print(center)
        
        color=(150,250,100)
        if i==len(coords)-4:
            color=(255,0,0)
        if obsz<(z1+vz[i]*dt):
            #cv2.circle(img,center,round(10/abs((coords[i][2])-2-obsz)),color,-1)
            cv2.circle(img,center,2,color,-1)
    
    cv2.imshow("Gravity", img)
    cv2.waitKey(1)
    
    if keyboard.is_pressed('w'):
        obsz+=10*speed
    if keyboard.is_pressed('s'):
        obsz-=10*speed
    if keyboard.is_pressed('a'):
        betax+=1
    if keyboard.is_pressed('d'):
        betax-=1
    if keyboard.is_pressed('up arrow'):
        obsy+=speed*-1
    if keyboard.is_pressed('down arrow'):
        obsy-=speed*-1
    if keyboard.is_pressed('right arrow'):
        obsx+=speed
    if keyboard.is_pressed('left arrow'):
        obsx-=speed
    
    #print(ax[5],ay[5])
    #print(a)
    #print(scale*round(x)+offx,scale*round(y)+offy)



