#include <iostream>
#include <string>

using namespace std;

// Deklarasi fungsi
void Biodataku(string nama, string pekerjaan, string email);
void BiodataAyahku(string nama, string pekerjaan, string email);
void BiodataIbuku(string nama, string pekerjaan, string email);

// Fucntion definition
void Biodataku(string nama, string pekerjaan, string email) {
    cout << "Biodataku:" << endl;
    cout << "Nama: " << nama << endl;
    cout << "Email: " << email << endl;
    cout << "Pekerjaan: " << pekerjaan << endl;
}

void BiodataAyahku(string nama, string pekerjaan, string email) {
    cout << "\nBiodata Ayahku:" << endl;
    cout << "Nama: " << nama << endl;
    cout << "Email: " << email << endl;
    cout << "Pekerjaan: " << pekerjaan << endl;
}

void BiodataIbuku(string nama, string pekerjaan, string email) {
    cout << "\nBiodata Ibuku:" << endl;
    cout << "Nama: " << nama << endl;
    cout << "Email: " << email << endl;
    cout << "Pekerjaan: " << pekerjaan << endl;
}

int main() {
    Biodataku("Komeng Sutoyo", "Software Developer", "komeng@gmail.com");
    BiodataAyahku("Asep Simanjuntak", "Insinyur", "asep@gmail.com");
    BiodataIbuku("Siti Zubaidah", "Dokter", "siti@gmail.com");

    return 0;
}
