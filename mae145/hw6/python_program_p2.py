#A12141970
#!/usr/bin/env python3
import math
import random
import matplotlib.pyplot  as plt
def sample_normal_distribution(mean,variance):
    b=math.sqrt(variance)
    tempsum=0.0
    for i in range(12):
        tempsum=tempsum+random.uniform(-b,b)
    y=((tempsum/2.0)+mean)
    return y

if __name__=='__main__':
    mean=100
    variance=15
    n_bins=400
    y=[]
    for j in range(10000):
        y.append(sample_normal_distribution(mean,variance))
    plt.hist(y,bins=n_bins)
    plt.xlabel("Value")
    plt.ylabel("Number of Samples")
    plt.show()
    plt.gcf().clear()

