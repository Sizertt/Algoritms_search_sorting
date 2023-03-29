from __future__ import division
import numpy as np
import math
 
def aimFunction(x):
    y=x**3-60*x**2-4*x+6
    return y
x=[i/10 for i in range(1000)]
y=[0 for i in range(1000)]
for i in range(1000):
    y[i]=aimFunction(x[i])
T=100 
Tmin=10 
x=np.random.uniform(low=0,high=1000)
k=50 
y=0
t=0
while T>=Tmin:
    for i in range(k):
        y=aimFunction(x)
        xNew=x+np.random.uniform(low=-0.055,high=0.055)*T
        if (0<=xNew and xNew<=100):
            yNew=aimFunction(xNew)
            if yNew-y<0:
                x=xNew
            else:
                p=math.exp(-(yNew-y)/T)
                r=np.random.uniform(low=0,high=1)
                if r<p:
                    x=xNew
    t+=1
    print (t)
    T=1000/(1+t)
print(x,aimFunction(x))
