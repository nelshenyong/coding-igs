#include <iostream>
using namespace std;
int main()
{
    int opsi, bil1, bil2;

    cout<<"Kalkulator\n";
    cout<<"Pilihan Operasi\n";
    cout<<"1. Penjumlahan (+)\n2. Pengurangan (-)\n3. Perkalian\n4. Pembagian (/)\n";

    cout<<"----------------------\n";
    cout<<"Pilih operasi: ";
    cin>>opsi;

    cout<<"Masukan bilangan 1: ";
    cin>>bil1;

    cout<<"Masukan bilangan 2: ";
    cin>>bil2;

    if(opsi == 1){
    cout<<"Hasil dari penjumlahan "<<bil1<<" + "<<bil2<<" = "<<bil1 + bil2;}

    else if(opsi == 2){
    cout<<"Hasil dari pengurangan "<<bil1<<" - "<<bil2<<" = "<<bil1 - bil2;}

    else if(opsi == 3){
    cout<<"Hasil dari perkalian "<<bil1<<" * "<<bil2<<" = "<<bil1 * bil2;}

    else if(opsi == 4){
    cout<<"Hasil dari pembagian "<<bil1<<" / "<<bil2<<" = "<<bil1 / bil2;}

    else{
    cout<<"Pilihan tidak sesuai!";}

}