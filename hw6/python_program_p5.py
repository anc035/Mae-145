#A12141970
import numpy as np
import math

def kinematic_properties(x,y,theta,vel_l,vel_r,t,L,R):
    v=(R*(vel_r+vel_l)/2.0)
    w=(R*(vel_r-vel_l)/L)
    try:
        radius_curvature=abs(v/w)
        ICCx=x-(v/w)*np.sin(theta)
        ICCy=y+(v/w)*np.cos(theta)
    except ZeroDivisionError:
        radius_curvature=math.inf
        ICCx=math.inf
        ICCy=math.inf
    return w,radius_curvature,[ICCx,ICCy]


if __name__=='__main__':
    command=(0.3,0.3,3.0)
    x=1.5
    y=2.0
    theta=np.pi/2.0
    L=0.5
    R=0.15

    omega,rad_curv,icc=kinematic_properties(x,y,theta,command[0],command[1],command[2],L,R)
    print(omega,rad_curv,icc)

