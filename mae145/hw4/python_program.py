#A12141970
#! /usr/bin/env/python
import math
import numpy as np
import matplotlib.pyplot as plt

def computeGridSukharev(n):
    #computes Sukharev grid in 2D square
    #compute number of intervals per axis
    if n<1:
        print('Negative number of n chosen')
        return [],[]
    k=math.sqrt(n)
    #pre allocate list for X and Y
    X=[]
    Y=[]
    Points=[]
    #calculate dispersion
    dispersionSquare=1/(2*k)
    for i in range(int(k)):
        for j in range(int(k)):
            X.append(2*i*dispersionSquare+dispersionSquare)
            Y.append(2*j*dispersionSquare+dispersionSquare)
    for index in range(len(X)):
        Points.append([X[index],Y[index]])
    plt.scatter(X,Y,color='r',marker='o')
    plt.title("Sukharev Grid")
    plt.xlim((0,1))
    plt.ylim((0,1))
    plt.show()
    return X,Y,Points
def computeGridRandom(n):
    X=np.random.sample(n)
    Y=np.random.sample(n)
    plt.scatter(X,Y,color='r',marker='o')
    plt.title("Random Grid")
    plt.xlim((0,1))
    plt.ylim((0,1))
    plt.show()
    return X,Y
def computeGridHalton(n,b1,b2):
    S1=np.zeros(n)
    S2=np.zeros(n)
    for i in range(n):
        temp1=i+1
        f1=1/b1
        temp2=i+1
        f2=1/b2
        while temp1 >0:
            QandR=divmod(temp1,b1)
            S1[i]=S1[i]+f1*QandR[1]
            temp1=QandR[0]
            f1=f1/b1
        while temp2 >0:
            QandR=divmod(temp2,b2)
            S2[i]=S2[i]+f2*QandR[1]
            temp2=QandR[0]
            f2=f2/b2
    plt.scatter(S1,S2,color='r',marker='o')
    plt.title("Halton Grid")
    plt.xlim((0,1))
    plt.ylim((0,1))
    plt.show()
    return S1,S2

    

if __name__=='__main__':
    X,Y,Points=computeGridSukharev(4)
    X,Y=computeGridRandom(4)
    X,Y=computeGridHalton(4,2,3)
