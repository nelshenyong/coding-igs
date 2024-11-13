#include <iostream>
using namespace std;
int main()
{
    int opsi, jumlah, harga, total;
    cout<<"Pilihan Kelas\n";
    cout<<"1. Kelas Ekonomi\n2. Kelas Bisnis\n3. Kelas Eksekutif\n";

    cout<<"----------------------\n";
    cout<<"Pilih operasi: ";
    cin>>opsi;

switch (opsi)
{

    case 1:
        harga = 150000;
        cout<<"\nHarga Tiket: " <<harga<<"/Orang\n";
        break;

    case 2:
        harga = 250000;
        cout<<"\nHarga Tiket: " <<harga<<"/Orang\n";
        break;

    case 3:
        harga = 375000;
        cout<<"\nHarga Tiket: "<<harga<<"/Orang\n";
        break;
    }
    cout<<"\nMasukan Jumlah: ";
    cin>>jumlah;
    total = harga * jumlah;
    cout<<"Total Bayar: Rp"<<total<<"/Orang";  
}