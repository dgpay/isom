import random
import numpy as np
from scipy.stats import norm


b=1.0
a=0.0
M=100
w=(b-a)/M
#print(w)
x=np.random.uniform(0, 1,M)
fxarr=[]
wfxarr=[]

def function_integral(xn,M,fxarr):
    i=0
    while i<M :
        fx=6*(xn[i]**2)
        fxarr.append(fx)
        i=i+1
    return fxarr

print('=====================ALGORITMA 1===============================')
def wfxarrfuct(w,M,fxarr,wfxarr):
    i=0
    while(i<M):
        wfxarr.append(fxarr[i]*w)
        i=i+1
    return wfxarr

def rectangular(M,wfxarr):
    i=0
    rectangular=0
    while(i<M):
        rectangular=rectangular+wfxarr[i]
        i=i+1
    return rectangular


function_integral(x,M,fxarr)
# print(xarr)
# print(fxarr)
wfxarrfuct(w,M,fxarr,wfxarr)
# print(wfxarr)
print(rectangular(M,wfxarr).round(2))
# print(np.linspace(0,1,101))
# print(np.random.uniform(0,1,100))

print(' ')
print('=====================ALGORITMA 2===============================')
print('')

k=norm.interval(0.95,0,1)
k1=norm.sf(0.95,0,1)
k2=norm.isf(0.95,0,1)
k3=0.95
k4=norm.ppf(0.95,0,1).round(2)


def function_rate(fxarr,M):
    i=0
    function_rate=0
    while(i<M):
        function_rate=function_rate+fxarr[i]
        i=i+1
    print("TOT",function_rate)
    return function_rate/M
def variansi(fxarr,frate,M):
    i=0
    variansi=0
    while(i<M):
        total=(fxarr[i]**2)-(frate**2)
        variansi=(variansi)+(total)
        i=i+1

    return (variansi)/(M-1)
def function_variansi(variansi,M):
    function_variansi=variansi/M
    return function_variansi

def batas_bawah(function_rate,function_variansi,k1):
    batas_bawah=((1-0)*((function_rate)-(k1*function_variansi)))
    return batas_bawah

def batas_atas(function_rate,function_variansi,k1):
    batas_atas=((1-0)*((function_rate)+(k1*function_variansi)))
    return batas_atas

# print(norm.interval(0.95,1,0))
# print(x)

# print(1-0)
# print(k4)

frate=function_rate(fxarr,M)
var=variansi(fxarr,frate,M)
fvar=function_variansi(var,M)
baw=batas_bawah(frate,fvar,k4)
at=batas_atas(frate,fvar,k4)
# print("k4 = ",k4)
# print(fxarr)
# print("rata-rata =",frate)
# print("var =",var)
# print("function var",fvar)
print(baw," <= I <=  ",at)


