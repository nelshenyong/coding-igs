#include <iostream>
using namespace std;

// Overloading Functions
double keliling(int r) {
    double hasil_keliling = 2 * 3.14 * r;
    return hasil_keliling;
}

// Prototype Function
double luas(int r);

int main() {
    int r;
    cout << "Masukkan Jari - Jari: "; cin >> r;
    double hasil_luas = luas(r);
    cout << "Luas lingkaran = " << hasil_luas << endl;
    cout << "Keliling lingkaran = " << keliling(r) << endl;
}

// Function Definition
double luas(int r) {
    double hasil_luas = 3.14 * r * r;
    return hasil_luas;
}