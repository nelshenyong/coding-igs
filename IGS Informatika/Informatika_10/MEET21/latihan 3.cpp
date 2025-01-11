#include <iostream>
using namespace std;

// Overloading Functions
// 4 * sisi
double luas(int sisi_bk) {
    double hasil_luas = 4 * sisi_bk;
    return hasil_luas;
}

// 0.5 x d1 x d2
double keliling(double diagonal1, double diagonal2) {
    double hasil_keliling = 0.5 * diagonal1 * diagonal2;
    return hasil_keliling;
}

int main() {
    int sisi;
    double d1, d2;
    cout << "Masukkan Panjang Sisi: "; cin >> sisi;
    cout << "\nMasukkan Nilai D1: "; cin >> d1;
    cout << "\nMasukkan Nilai D2: "; cin >> d2;
    cout << "Luas belah ketupat = " << luas(sisi) << endl; 
    cout << "Luas belah ketupat = " << luas(d1, d2) << endl; 
}