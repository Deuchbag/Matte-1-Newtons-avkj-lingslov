
import numpy as np
import matplotlib.pyplot as plt

# Noah Matheson Havneraas
t_verdier = [0,60,120,180,240,300,360,420,480,540,600]
temp_verdier = [83.4,74.2,72.0,66.9,63.9,61.2,58.0,56.4,54.7,52.7,51.7]
T_verdier = []
tid_verdier = np.linspace(0,600,1000)


def T(t):
    return 63.2*np.exp(alpha_verdi*t)+20.2

def alpha(y,t):
    return (np.log((y-20.2)/63.2))/t 

alpha_verdi = alpha(temp_verdier[10],600)

for i in range(len(tid_verdier)):
    T_verdier.append(T(i))

plt.plot(tid_verdier,T_verdier, label = "Noah: teoretisk avkjøling")
plt.plot(t_verdier,temp_verdier, label = "Noah: faktisk avkjøling")



# Roberts Naumenko
def Roberts_alpha(y,t):
     return (np.log((y-21)/78.9))/t 

def Roberts_Newton(t):
    return 78.9*np.exp(Roberts_alpha_verdi*t)+21


Temp_verdier = [99.9,87.2,86.2,82.2,79.9,76.9,74.5,72.2,70.0,68.4,66.6]

Roberts_alpha_verdi = Roberts_alpha(Temp_verdier[10],600)
teoretisk_verdier = []



for i in range(len(tid_verdier)):
    teoretisk_verdier.append(Roberts_Newton(i))

print(f"Noah sin alpha verdi ble: {alpha_verdi}")
print(f"Robert sin alpha verdi ble: {Roberts_alpha_verdi}")

plt.plot(tid_verdier, teoretisk_verdier,label = "Roberts: teoretisk avkjøling")
plt.plot(t_verdier,Temp_verdier, label = "Roberts: faktisk avkjøling")
plt.grid(True)
plt.xlabel("t(s)")
plt.ylabel("Temperatur(celsius)")
plt.legend()
plt.show() 