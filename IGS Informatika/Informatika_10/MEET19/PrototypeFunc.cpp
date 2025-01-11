#include <iostream>
using namespace std;

void Heiii();
double Luas_segitiga(int alas, double tinggi);

int main(){
    Heiii();
    Heiii();
    Heiii();
    cout << "Luas segitiga: " << Luas_segitiga(12, 36) << endl;
}

// Function Definition
void Heiii(){
    cout<< "Hei.. Selamat Siang..." << endl;
}

double Luas_segitiga(int alas, double tinggi){
    double hasil = 0.5 * alas * tinggi;
    return hasil;
}