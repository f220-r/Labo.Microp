#include "matematica.h"
#include <iostream>

using namespace std;


int main(void) {
	cout << "Probando multip inline: " << Multiplicar_Sat(2, 2) << endl;
	cout << "Direcc variable global: " << &c_a_count << endl;
    return 0;
}