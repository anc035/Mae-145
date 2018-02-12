#A12141970
#! /usr/bin/env python
import math

def computeDistanceOnCircle(theta1, theta2):
    #set error flag to 0
    error=0
    counterDistance=theta2-theta1
    clockDistance=theta1-theta2
    #test if points are far enough apart
    if abs(counterDistance) <1e-3 or abs(clockDistance) <1e-3:
        print('Cannot compute distance, points are too close together')
        error=1
        return 0
    #compute the counter and clockwise distances 
    if error==0:
        if counterDistance<0:
           counterDistance= counterDistance % (2*pi)
        if clockDistance <0:
            clockDistance=clockDistance %(2*pi)
        #return the shortest one
        return min(clockDistance,counterDistance)

def computeDistanceOnTorus(alpha1, alpha2,beta1,beta2):
    alphadist=computeDistanceOnCircle(alpha1,alpha2) 
    betadist=computeDistanceOnCircle(beta1,beta2)
    #check if error was flagged in computing distance
    if alphadist==0 or betadist==0:
        return 0
    distanceT=math.sqrt((alphadist**2)+(betadist**2))
    return distanceT
if __name__=='__main__':
    pi=math.pi
    theta1=pi
    theta2=pi/2
    distance=computeDistanceOnCircle(theta1,theta2)
    print(distance)
    alpha1,beta1=pi/3,pi/6
    alpha2,beta2=pi,pi/2
    distanceT=computeDistanceOnTorus(alpha1,alpha2,beta1,beta2)
    print(distanceT)
