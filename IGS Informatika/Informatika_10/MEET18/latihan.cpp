#include <iostream>
using namespace std;
double rumusku( int p ,int l){
    int hasil = 2 * (p + l);
    return hasil;
}

double rumusku2( int p ,int l){
    int hasil2 = p * l;
    return hasil2;
}

void tampil(double hasil){
    cout << "Hasil luas bangun datar persegi panjang = "<< hasil << "\n ";
}

void tampil2(double hasil2){
    cout << "Hasil keliling bangun datar persegi panjang = " << hasil2;
}

int main(){
    int p_1, l_1;
    cout << "Nilai panjang = "; cin >> p_1;
    cout << "Nilai lebar = "; cin >> l_1;
    tampil(rumusku(p_1, l_1));
    tampil2(rumusku2(p_1, l_1));
}