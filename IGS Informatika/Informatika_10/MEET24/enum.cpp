#include <iostream>
using namespace std;
// Enumerate : sebuah tipe data yang berguuna untuk menyimpan sekumpullan var, const

enum warna {hijau, kuning, merah, biru = 10};
int main()
{
    cout<<"Hijau = "<<hijau<<endl;
    cout<<"kuning = "<<kuning<<endl;
    cout<<"merah = "<<merah<<endl;
    cout<<"biru = "<<biru<<endl;
    warna baju;
    baju = merah;
    cout << "baju = "<<baju<<endl;

    return 0;
}       