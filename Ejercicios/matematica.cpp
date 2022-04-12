#include "matematica.h"

#include<iostream>

using namespace std;

uint16_t c_a_count = 0;

int32_t Sumar_Array(int16_t* x, int16_t xn) {
	int32_t res = 0;
	for (int16_t i = 0; i < xn; i++) {
		res = res + x[i];
	}
	return res;
}


int16_t Multiplicar_Sat(int16_t n1, int16_t n2) {
	int16_t const SAT16_MAX = 32767;
	int16_t const SAT16_MIN = -32767;
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




uint16_t Cuenta_Accesos(void) {
	return c_a_count++;
}