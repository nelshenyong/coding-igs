#include <iostream>
using namespace std;
int main()
{
    int opsi, jumlah;
    cout<<"Pilihan Kelas\n";
    cout<<"1. Kelas Ekonomi\n2. Kelas Bisnis\n3. Kelas Eksekutif\n";

    cout<<"----------------------\n";
    cout<<"Pilih operasi: ";
    cin>>opsi;

    if(opsi == 1){
    cout<<"Harga Tiket: Rp150.000"<<endl;
    cout<<"Masukan Jumlah: ";
    cin>>jumlah;
    cout<<"Total Bayar:  Rp"<<150000 * jumlah;}

    else if(opsi == 2){
    cout<<"Harga Tiket: Rp250.000"<<endl;
    cout<<"Masukan Jumlah: ";
    cin>>jumlah;
    cout<<"Total Bayar:  Rp"<<250000 * jumlah;}

    else if(opsi == 3){
    cout<<"Harga Tiket: Rp375.000"<<endl;
    cout<<"Masukan Jumlah: ";
    cin>>jumlah;
    cout<<"Total Bayar:  Rp"<<375000 * jumlah;}

    else{
    cout<<"Pilihan tidak sesuai!";}
}