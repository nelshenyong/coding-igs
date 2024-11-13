#include <iostream>
using namespace std;

int main() {
    string nama;
    int umur, kelas;
    int tahun = 2023;

    cout << "Nama: ";
    cin >> nama;

    cout << "Umur: ";
    cin >> umur;

    cout << "Kelas: ";
    cin >> kelas;

    cout << "" << endl;
    cout << "Say my name (3x):" << endl;

    for (int i = 1; i <= 3; i++) {
        cout << i << ". " << nama << endl;
    }

    cout << "------------------------" << endl;
    while (tahun <= 2026) {
        cout << "My age in " << tahun << ": " << umur << " tahun" << endl;
        tahun++;
        umur++;
    }

    tahun = 2023; 

    cout << "------------------------" << endl;
    do {
        cout << "My class in " << tahun << ": " << kelas << endl;
        tahun++;
        kelas++;
    } while (tahun <= 2026);

    return 0;
}