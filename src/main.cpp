 
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main (void) {
    fstream newfile;
   newfile.open("text_file.txt",ios::in); //open a file to perform read operation using file object
   if (newfile.is_open())
    { //checking whether the file is open
        string tp;
        while(getline(newfile, tp)){ //read data from file object and put it into string.
        cout << tp << "\n"; //print the data of the string
    }
    newfile.close(); //close the file object.
   }
   cout<< "==================================" << endl;
   cout<< "========= Fin del programa ========"<<endl;


}

/*

build command: g++ -o build/app.exe src/main.cpp
*/