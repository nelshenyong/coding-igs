#include <iostream>
using namespace std;

int main() {
    int a, b, hasil, jawab;
    cout << "Masukkan angka 1: ";
    cin >> a;
    cout << "Masukkan angka 2: ";
    cin >> b;
    cout << "Berapa hasil dari " << a << " + " << b << "?\n";
    cout << "Jawab: ";
    cin >> jawab;
    hasil = a + b;
    if (jawab == hasil) {
        cout << "Jawaban benar!" << endl;
    } else {
        cout << "Jawaban salah!" << endl;
    }
    return 0;
}