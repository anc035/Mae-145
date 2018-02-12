#A12141970
#! /usr/bin/env python
import math

def distanceform(p1,p2):
    dx=float(p2[0])-float(p1[0])
    dy=p2[1]-p1[1]
    length=math.sqrt(dx**2+dy**2)
    return length

def computeLineThroughTwoPoints(p1,p2):
    #test points are far enough
    distance=distanceform(p1,p2)
    error =0
    if distance <1e-5:
        print('Cannot compute line: two points too close')
        error =1
        return 0,0,0
    if error ==0:
        a=p1[1]-p2[1]
        b=p2[0]-p1[0]
        c=p1[0]*p2[1]-p2[0]*p1[1]
        return a/distance,b/distance,c/distance

def computeDistancePointToLine(q,p1,p2):
    a,b,c=computeLineThroughTwoPoints(p1,p2)
    num=abs(a*q[0]+b*q[1]+c)
    den=math.sqrt(a**2+b**2)
    d=num/den
    return d

def computeDistancePointToSegment(q,p1,p2):
    seglength=distanceform(p1,p2)
    u=((q[0]-p1[0])*(p2[0]-p1[0])+(q[1]-p1[1])*(p2[1]-p1[1]))/(seglength**2)
    if 0.0 <=u<=1.0:
        D=computeDistancePointToLine(q,p1,p2)
        wP=0
    elif u<0.0:
        D=distanceform(q,p1)
        wP=1
    else:
        D=distanceform(q,p2)
        wP=2
    return D
if __name__ == '__main__':
    p1=[0,0]
    p2=[2,5]
    q=[2,8]
    computeLineThroughTwoPoints(p1,p2) 
    d=computeDistancePointToLine(q,p1,p2)
    print(d)
    dist=computeDistancePointToSegment(q,p1,p2)
    print(dist)
