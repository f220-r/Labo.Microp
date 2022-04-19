#ifndef _FUNCIONES_MAT_
#define _FUNCIONES_MAT_

#include "stdint.h"
#include <iostream>

using namespace std;

extern uint16_t c_a_count; 
int32_t Sumar_Array(int16_t* x, int16_t xn);
inline int16_t Multiplicar_Sat(int16_t n1, int16_t n2) {
	int16_t const SAT16_MAX = 32767;
	int16_t const SAT16_MIN = -32768;
	int32_t r_aux = n1*n2;
	int16_t res = n1*n2;
	if (r_aux > SAT16_MAX) {
		cout << "Error: valor máximo superado" << endl;
		return(-1);
	}
	else if (r_aux < SAT16_MIN) {
		cout << "Error: valor mínimo superado" << endl;
		return(-1);
	}
	return(res);
}
uint16_t Cuenta_Accesos(void);

#endif //_FUNCIONES_MAT_