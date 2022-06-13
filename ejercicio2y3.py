import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
import csv

##----------------------------------------------------Inicio ejercicio 2

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

plt.figure(1)
plt.title('Funciones en tiempo')
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

##----------------------------------------------------Inicio ejercicio 3

#D1(8 bits)
N1 = 8
D1_min = 0
D1_max = 2^N1 -1

D1 = np.round( S2 * (D1_max/Vmax)) 
D1_f =  S2 * (D1_max/Vmax)
E1 = D1 - D1_f
print('D1: ',D1[0:10])
print('D2: ',D1_f[0:10])
print('D3: ',E1[0:10])

#D2(12 bits)
N2 = 12
D2_min = 0
D2_max = 2^N2 -1

D2 = np.round( S2 * (D2_max/Vmax)) 
D2_f =  S2 * (D2_max/Vmax)
E2 = D2 - D2_f
#D3(24 bits)
N3 = 24
D3_min = 0
D3_max = 2^N3 -1

D3 = np.round( S2 * (D3_max/Vmax)) 
D3_f =  S2 * (D3_max/Vmax)
E3 = D3 - D3_f


plt.figure(2)
# Primer Gráfico :
im1 = plt.subplot (3,1,1) 
plt.plot(t, D1, color)    
plt.plot(t, D1_f, 'g')
plt.plot(t, E1, 'r')    
plt.grid(True)                                                                    
plt.xlabel('[s]')                                                         
plt.title("Señal D1")

# Segundo Gráfico :
im1 = plt.subplot (3,1,2) 
plt.plot(t, D2, color)    
plt.plot(t, D2_f, 'g')
plt.plot(t, E2, 'r')    
plt.grid(True)                                                                    
plt.xlabel('[s]')                                                         
plt.title("Señal D2")

# Tercer Gráfico :
im1 = plt.subplot (3,1,3) 
plt.plot(t, D3, color)    
plt.plot(t, D3_f, 'g')
plt.plot(t, E3, 'r')    
plt.grid(True)                                                                    
plt.xlabel('[s]')                                                         
plt.title("Señal D3")
plt.savefig("figura3_1.png")    
plt.show()

Fs = 500 #Hz
color = 'b'                                      
N = D1.size                             
res = float(Fs / (N-1)) #Resolucion frecuencial
n = np.array(range(0, N)) * res  

espectro1 = fft(D1)                                                        
modulo1  = np.absolute(espectro1) 

espectro2 = fft(D2)                                                        
modulo2  = np.absolute(espectro1) 

espectro3 = fft(D3)                                                        
modulo3  = np.absolute(espectro3) 

# Primer Gráfico :
plt.figure(3)
im1 = plt.subplot (3,1,1) 
plt.plot (n, modulo1, color)                
plt.grid(True)    
plt.xlabel ('f[Hz]' )

# Segundo Gráfico :
im1 = plt.subplot (3,1,2) 
plt.plot (n, modulo2, color)                
plt.grid(True)    
plt.xlabel ('f[Hz]' )

# Tercer Gráfico :
im1 = plt.subplot (3,1,3) 
plt.plot (n, modulo3, color)                
plt.grid(True)    
plt.xlabel ('f[Hz]' )
plt.savefig("figura3_2.png")    
plt.show()