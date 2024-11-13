#include <iostream>
using namespace std;
int main()
{
    int opsi, r, a, t, p, l, d1, d2;

    cout<<"Pilihan Operasi\n";
    cout<<"1. Luas Lingkaran\n2. Luas Segitiga\n3. Luas Persegi Panjang\n4. Luas Belah Ketupat\n";

    cout<<"----------------------\n";
    cout<<"Pilih operasi: ";
    cin>>opsi;

    if(opsi == 1){
    cout<<"Masukan nilai r: ";
    cin>>r;
    cout<<"Hasil luas = "<<3.14 * (r * r);}

    else if(opsi == 2){
    cout<<"Masukan nilai a: ";
    cin>>a;
    cout<<"Masukan nilai t: ";
    cin>>t;
    cout<<"Hasil luas = "<<0.5 * (a * t);}

    else if(opsi == 3){
    cout<<"Masukan nilai p: ";
    cin>>p;
    cout<<"Masukan nilai l: ";
    cin>>l;
    cout<<"Hasil luas = "<<p * l;}

    else if(opsi == 4){
    cout<<"Masukan nilai d1: ";
    cin>>d1;
    cout<<"Masukan nilai d2: ";
    cin>>d2;
    cout<<"Hasil luas = "<<0.5 * (d1 * d2);}

    else{
    cout<<"Pilihan tidak sesuai!";}

}