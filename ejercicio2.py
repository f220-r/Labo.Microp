import numpy as np
import matplotlib.pyplot as plt
import csv

rango = [1,-1]
Vmax = 3.3 - .1
Vmin = 0.0 - .1

G = (Vmax - Vmin) / (rango[0] - rango[1])   #ganancia
k = (Vmax - Vmin) / 2                       #offset

with open('presion_tp1.csv', newline='') as f:
    reader = csv.reader(f)
    presion = list(reader)

S1 = np.array(presion,dtype=float)
S2 = S1*G + k

Fs = 500 #Hz
color = 'b'                                      
N = len(presion)                                                     
Ts = 1 / Fs                                                                
k2 = np.array(range(0,N))                                                              
t = (k2 * Ts)                                                                                                        


# Primer Gráfico :
im1 = plt.subplot (2,1,1) 
plt.plot(t, S1, color)             
plt.grid(True)                                                                    
plt.xlabel('[s]')                                                             
#titulo = "%s N = %d Fs = %.2f [Hz]" %(titulo, N, Fs)                     
plt.title("Señal 1 en funcion del tiempo")

# Segundo Gráfico :
im1 = plt.subplot (2,1,2) 
plt.plot(t, S2, color)             
plt.grid(True)                                                                    
plt.xlabel('[s]')                                                             
#titulo = "%s N = %d Fs = %.2f [Hz]" %(titulo, N, Fs)                     
plt.title("Señal 2 en funcion del tiempo")

plt.savefig("figura2.png")    
plt.show()
