#A12141970
import numpy as np

def predict_next_pos(x,y,theta,vel_l,vel_r,t,L,R):
    w=(R*(vel_r-vel_l)/L)
    v=(R*(vel_r+vel_l)/2.0)
    if(vel_l==vel_r):
        xPrime=x-v*t*np.cos(theta)
        yPrime=y+v*t*np.sin(theta)
        thetaPrime=theta
    else:
        xPrime=x-(v/w)*np.sin(theta)+(v/w)*np.sin(theta+w*t)
        yPrime=(v/w)*np.cos(theta)-(v/w)*np.cos(theta+w*t)
        thetaPrime=w*t
    return xPrime,yPrime,thetaPrime


        


if __name__=='__main__':
    command=(0.3,0.3,3)
    L=0.5
    R=0.15
    x=1.5
    y=2.0
    theta=1.5707
    [x_1,y_1,theta_1]=predict_next_pos(x,y,theta,command[0],command[1],command[2],L,R)
    print(x_1,y_1,theta_1)



