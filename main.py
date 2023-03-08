import matplotlib.pyplot as plt
import numpy as np
import time
import random
from scipy.optimize import curve_fit

def buscarParejas(arr, suma):
    parejas = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == suma:
                parejas.append((arr[i],arr[j]))
    return parejas

def generarRandomList(n):
    arr = []
    for i in range (n):
        arr.append(random.randint(0,2*n))
    return arr

def ajuste(x,y):
    #Aca esta haciendo un ajuste cuadratico
    z = np.polyfit(x,y,2)
    p = np.poly1d(z)
    #la linea va a ser roja y punteada
    plt.plot(x,p(x), 'r--')
    plt.grid()
    plt.show()

suma = -1
random.seed(1234)
tiempos = []
n = []

N = 100
for i in range (1, N+1):
    arr=generarRandomList(i)
    n.append(i)
    start = time.perf_counter()
    buscarParejas(arr, suma)
    end = time.perf_counter()
    tiempos.append(end-start)

#plt.scatter se utiliza para graficar en puntos
plt.scatter(n,tiempos)
plt.show()

ajuste(n, tiempos)