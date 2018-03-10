#A12141970
import math
import python_program_p2 as pp2
import numpy as np
import matplotlib.pyplot as plt

pi=math.pi

def sampleNorm(variance):
    return pp2.sample_normal_distribution(0,variance)

def predict(x_t,u_t_plus_1,alpha):
    delt_hat_r1=u_t_plus_1[0]-sampleNorm(alpha[0]*(u_t_plus_1[0]**2)+alpha[1]*(u_t_plus_1[1]**2))
    delt_hat_r2=u_t_plus_1[1]-sampleNorm(alpha[0]*(u_t_plus_1[0]**2)+alpha[1]*(u_t_plus_1[1]**2))
    delt_hat_trans=u_t_plus_1[2]-sampleNorm(alpha[2]*(u_t_plus_1[2]**2)+alpha[3]*(u_t_plus_1[0]**2)+alpha[3]*(u_t_plus_1[1]**2))
    xPrime=x_t[0]+delt_hat_trans*math.cos(x_t[2]+delt_hat_r1)
    yPrime=x_t[1]+delt_hat_trans*math.sin(x_t[2]+delt_hat_r1)
    thetaPrime=x_t[2]+delt_hat_r1+delt_hat_r2
    return np.array([xPrime,yPrime,thetaPrime])



if __name__=='__main__':
    x_t=[2.0,4.0,0.0]
    u_t_plus_1=[pi/2.0,0.0,1.0]
    alpha=[.1,.1,.01,.01]
    sample_num=5000
    x_t_plus_1=np.zeros([sample_num,3])
    for i in range(0,sample_num):
        x_t_plus_1[i,:]=predict(x_t,u_t_plus_1,alpha)
    plt.plot(x_t[0],x_t[1],'.g')
    plt.plot(x_t_plus_1[:,0],x_t_plus_1[:,1],".r")
    plt.xlabel("x-pose [m]")
    plt.ylabel("y-pose [m]")
    plt.show()
    plt.gcf().clear()
