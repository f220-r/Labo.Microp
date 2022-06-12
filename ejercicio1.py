import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq
import csv


with open('presion_tp1.csv', newline='') as f:
    reader = csv.reader(f)
    presion = list(reader)

Fs = 500 #Hz
snl = presion
color = 'b'                                      
N = len(snl)                                                     
Ts = 1 / Fs                                                                
k = np.array(range(0,N))                                                              
t = (k * Ts)                                                   

img = plt.figure ()
espectro = fft(snl)                                                        

modulo  = np.absolute(espectro)                                               
res = float(Fs / (N-1)) #Resolucion frecuencial
n = np.array(range(0, N)) * res                                                       

# Primer Gráfico :
im1 = plt.subplot (2, 1, 1) 
plt.plot (n, modulo, color)                
plt.grid(True)    
plt.xlabel ('f[Hz]' )
plt.title('Módulo del espectro de la señal' ) 

# Segundo Gráfico :
im1 = plt.subplot (2,1,2) 
snl = np.array(snl,dtype=float)
plt.plot(t, snl, color)             
plt.grid(True)                                                                    
plt.xlabel('[s]')                                                             
#titulo = "%s N = %d Fs = %.2f [Hz]" %(titulo, N, Fs)                     
plt.title("Señal en funcion del tiempo")

plt.savefig("figura1.png")    
plt.show()