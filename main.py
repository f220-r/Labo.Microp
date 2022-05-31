from attr import asdict
import numpy as np

def saludar(nom):
    if (nom == ''):
        print('hola anonimus')
    else:
        print(f'hola {nom}')

ms1 = 'hola'
ms2 = 'mundo'

v1 = 10
v2 = 30


print(ms1+ms2)

print(v1 + v2**2)

a2 = [1, 2, 3]
#print (a2)

tupla = (1,2,3)
print(tupla)

a3 = np.array([1,2,3])
print(a3 * 2)

if(v1 >= 11):
    print('Estoy adentro del if')
elif (v1 == 10):
    print('v1 vale 10')
else:
    print('Estoy afuera del if')

saludar('Flor')