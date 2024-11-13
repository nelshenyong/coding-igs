#include <iostream>
#include <string>
#include <cmath>
using namespace std;

double tambah(int angka_1, double angka_2);
double kurang(int angka_1, double angka_2);
double kali(int angka_1, double angka_2);
double pangkat(int angka_1, double angka_2);

int main(){
    cout << "-=----- HITUNGKU ------" << endl;
    cout << "1. Tambah  2.Kurang" << endl;
    cout << "3. Kali  4. Pangkat" << endl;
    cout << "-------------------------" << endl;
    string opsi;
    int angka_1, angka_2;
    cout << "\n Pilihan: ";
    cin >> opsi;
    cout << "-------------------------" << endl;
    cout << "Masukkan nilai 1: "; cin >> angka_1;
    cout << "\nMasukkan nilai 2: "; cin >> angka_2;
    cout << "-------------------------" << endl;
    if (opsi == "1") {
        double hasil = tambah(angka_1, angka_2);
        cout << "Hasil" << angka_1 << " + " <<  angka_2 << " = " << hasil;
    }
    else if (opsi == "2") {
        double hasil = kurang(angka_1, angka_2);
        cout << "Hasil " << angka_1 << " - " <<  angka_2 << " = " << hasil;
    }
    else if (opsi == "3") {
        double hasil = kali(angka_1, angka_2);
        cout << "Hasil " << angka_1 << " * " <<  angka_2 << " = " << hasil;
    }
    else if (opsi == "4") {
        double hasil = pangkat(angka_1, angka_2);
        cout << "Hasil " << angka_1 << " ^ " <<  angka_2 << " = " << hasil;
    }
}

// Function Definition

double tambah(int angka_1, double angka_2){
    double hasil = angka_1 + angka_2;
    return hasil;
}

double kurang(int angka_1, double angka_2){
    double hasil = angka_1 - angka_2;
    return hasil;
}

double kali(int angka_1, double angka_2){
    double hasil = angka_1 * angka_2;
    return hasil;
}

double pangkat(int angka_1, double angka_2){
    double hasil = pow(angka_1, angka_2);
    return hasil;
}