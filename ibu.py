import numpy as np

b=1.0
a=0.0
M=100

def easy(x):
    return((6)*(x**2))

def integrated(a,b,func=easy,n=10000):
    dx=(b-a)/n
    Xs=np.linspace(a,b,n+1)
    return(np.sum(func(Xs))*dx)

print(integrated(a,b,easy))