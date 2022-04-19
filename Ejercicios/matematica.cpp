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







uint16_t Cuenta_Accesos(void) {
	return c_a_count++;
}