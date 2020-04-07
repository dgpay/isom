import random
import numpy as np



b=1.0
a=0.0
M=100
w=(b-a)/M
#print(w)
x=np.linspace(0,1,101)
print(x)

fxarr=[]
wfxarr=[]

def function_integral(x,M,fxarr):
    i=0
    while i<=M :
        fx=(6)*(x[i]**2)
        fxarr.append(fx)
        i=i+1
    return fxarr
def wfxarrfuct(w,M,fxarr,wfxarr):
    i=0
    while(i<=M):
        wfxarr.append(fxarr[i]*w)
        i=i+1
    return wfxarr

def rectangular(M,wfxarr):
    i=0
    rectangular=0
    while(i<=M):
        rectangular=rectangular+wfxarr[i]
        i=i+1
    return rectangular

function_integral(x,M,fxarr)
# print(xarr)
# print(fxarr)
wfxarrfuct(w,M,fxarr,wfxarr)
# print(wfxarr)
print(rectangular(M,wfxarr))