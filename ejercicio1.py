import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq
import csv

def  Margenes(sgn, margen_porcentual ):

    maximo = max(sgn )                                                         # Máximo de la señal a graficar
    minimo = min(sgn )                                                         # Mínimo de la señal a graficar

    span = maximo - minimo                                                    # Rango dinámico de la señal

    if(span == 0):
        span = 1                                                               # Fuerzo el span si las señales tienen sus muestras iguales
    

    margen = margen_porcentual * abs(span ) 

    maximo = maximo + margen 
    minimo = minimo - margen 

    return [maximo, minimo]


with open('presion_tp1.csv', newline='') as f:
    reader = csv.reader(f)
    presion = list(reader)

Fs = 500 #Hz
snl = presion
color = 'b'
mod_gr = 1
NF = 1
NC = 2
G0 = 1
t0 = 0

margenY = 0.1                                                              # Margen porcentual en el eje y
N = len(snl)                                                     # Calculo la longitud de la señal

Ts = 1 / Fs                                                                # Período de muestreo
k = np.array(range(0,N))                                                              # Eje de muestras
t = (k * Ts) + t0                                                  # Convierto de muestras a unidad de tiempo

xmin = t0                                                                  # Instante inicial de la señal
xmax = N*Ts + t0                                                     # Instante final de la señal


img = plt.figure ()
espectro = fft(snl)                                                        # Hago la fft de la señal

modulo  = np.absolute(espectro)                                                # Calculo el módulo de las muestras
fase    = np.angle(espectro)                                              # Calculo la fase del espectro de la señal

max_mod = max(modulo)                                                  # Calculo el máximo del módulo para normalizar
modulo_norm = modulo/max_mod                                           # Normalizo en función del máximo que me queda igual a uno
modulo_db = 20*np.log(modulo_norm)                                        # Convierto todo a dB (el máximo pasa a ser cero)

g1 = modulo_db                                                         # Guardo el módulo de la señal a graficar
g2 = fase                                                              # Guardo la fase de la señal a graficar
    
titulo = ''                      # Título general
tit1 = 'Módulo del espectro de la señal'                               # Titulo gráfico modulo
tit2 = 'Fase del espectro de la señal'                                 # Título gráfico fase
ylab1 = '|X(\omega)| [dB]'                                             # Etiqueta del eje vertical del primer gráfico
ylab2 = '\phi[X(\omega)] [rad]'                                        # Etiqueta del eje vertical del segundo gráfico

n = np.array(range(0, N)) * float(Fs / N)                                                        # Eje con número de muestras

## Correción de márgenes
[max1, min1 ] = Margenes(g1, margenY ) 
[max2, min2 ] = Margenes(g2, margenY )      
G0 = 1

NF = 2
NC = 1

# Primer Gráfico :
im1 = plt.subplot (NF, NC, G0) 
plt.plot (n, g1, color, 'LineWidth', 2 )                
plt.grid(True)    
plt.ylim ([min1,max1 ] ) 

plt.xlabel ('f[Hz]' )
plt.ylabel (ylab1) 
plt.title(tit1 ) 
# Segundo Gráfico :
im1 = plt.subplot (NF, NC, G0 + 1) 
snl = np.array(snl,dtype=float)
plt.plot(t, snl, color, 'LineWidth', 2)             
maximo = max(snl)                                                          # Maximo de la señal a graficar
minimo = min(snl)                                                          # Minimo de la señal a graficar

span = maximo - minimo ;                                                    # Rango dinamico de la señal

if(span == 0):                                                               # Si la señal tiene todas las muestras iguales el span es cero y da error
    span = 1                                                               # Fuerzo el span para poder ver correctamente la señal


margen_porcentual = 0.1                                                    # Margen del gráfico a mostrar más allá de sus límites
margen = margen_porcentual * abs(span)                                     # Genero el margen para sumar a los límites del gráfico

maximo = maximo + margen                                                   # Calculo el máximo del gráfico
minimo = minimo - margen                                                   # Calculo el mínimo del gráfico    

plt.ylim(minimo, maximo)                                                      # Límites del eje vertical
plt.xlim(xmin, xmax)                                                          # Limites del eje horizontal

plt.grid(True)                                                                    # Muestro la grilla sobre el fondo del gráfico
plt.xlabel('Tiempo [s]')                                                              # Asigno las etiqueta del eje X
plt.ylabel('Voltaje [V]]')                                                              # Asigno las etiqueta del eje Y
titulo = "Señal en funcion del tiempo"
#titulo = "%s N = %d Fs = %.2f [Hz]" %(titulo, N, Fs)                     # Genero la leyenda a escribir como título
plt.title(titulo)
plt.savefig("figura1.png")    
plt.show()