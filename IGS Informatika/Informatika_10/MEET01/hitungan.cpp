#include <iostream>
using namespace std;

int main()
{
    int a, b, c;
    a = 12;
    b = 3;

    // Operasi Penjumlahan
    cout << "Penjumlahan"<< endl;
    c = a + b;
    cout<<"Hasil dari "<<a<<" + "<<b<<" = "<<c<< endl;

    // Operasi Pengurangan
    c = a - b;
    cout << "Pengurangan"<< endl;
    cout<<"Hasil dari "<<a<<" - "<<b<<" = "<<c<< endl;

    // Operasi Perkalian
    c = a * b;
    cout << "Perkalian"<< endl;
    cout<<"Hasil dari "<<a<<" * "<<b<<" = "<<c<< endl;

    // Operasi Pembagian
    c = a / b;
    cout << "Pembagian"<< endl;
    cout<<"Hasil dari "<<a<<" / "<<b<<" = "<<c<< endl;

    // Operasi Modulo
    c = a % b;
    cout << "Pembagian"<< endl;
    cout<<"Hasil dari "<<a<<" % "<<b<<" = "<<c<< endl;

}