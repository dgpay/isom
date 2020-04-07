import numpy as np
from scipy.stats import norm
b=1
a=0
M=100
arrfx=[]
x=np.random.uniform(a, b,M)
k=norm.interval(0.95,0,1)
k1=norm.sf(0.95,0,1)
k2=norm.isf(0.95,0,1)
k3=0.95
k4=norm.ppf(0.95,0,1).round(2)
# def easy(x):
#     return(x+1)
# rate=np.sum(easy(x)+1)/M
def function_arr(arrfx,x,M):
    i=0
    while(i<M):
        fx=((6)*(x[i]**2))
        arrfx.append(fx.round(2))
        i=i+1
    return arrfx
def function_rate(arrfx,M):
    i=0
    function_rate=0
    while(i<M):
        function_rate=function_rate+arrfx[i]
        i=i+1
    print("TOT",function_rate)
    return function_rate/M
def variansi(arrfx,frate,M):
    i=0
    variansi=0
    while(i<M):
        variansi=(variansi)+(arrfx[i])
        i=i+1
    total=(variansi**2)-(M*(frate**2))
    return (total)/(M-1)
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
print(x)

# print(1-0)
# print(k4)
arrfx=function_arr(arrfx,x,M)
frate=function_rate(arrfx,M)
var=variansi(arrfx,frate,M)
fvar=function_variansi(var,M)
baw=batas_bawah(frate,fvar,k4)
at=batas_atas(frate,fvar,k4)
print("k4 = ",k4)
print(arrfx)
print("rata-rata =",frate)
print("var =",var)
print("function var",fvar)
print(baw,"    ",at)


