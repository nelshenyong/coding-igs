#include <iostream>
using namespace std;

int main()
{
    struct {
        char nama[50], sekolah[50], kelas[50], alamat[50];
    } biodata;
    cout<<"Masukkan nama anda: ";
    cin.getline(biodata.nama, 50);

    cout<<"Masukkan sekolah anda: ";
    cin.getline(biodata.sekolah, 50);

    cout<<"Masukkan kelas anda: ";
    cin.getline(biodata.kelas, 50);

    cout<<"Masukkan alamat anda: ";
    cin.getline(biodata.alamat, 50);

    cout<<"Halo! nama saya "<<biodata.nama<<" saya bersekolah di "<<biodata.sekolah<<" kelas "<<biodata.kelas<<" alamat saya di "<<biodata.nama<<endl;

    cout<<"------------------";

    struct
    {
        char baju[50], celana[50], sepatu[50], tas[50];
    } outfit;
    cout<<"Masukkan ukuran baju anda: ";
    cin.getline(biodata.baju, 50);

    cout<<"Masukkan ukuran celana anda: ";
    cin.getline(biodata.celana, 50);

    cout<<"Masukkan ukuran sepatu anda: ";
    cin.getline(biodata.sepatu, 50);

    cout<<"Masukkan tas anda: ";
    cin.getline(biodata.tas, 50);

    cout<<"Ukuran baju saya "<<biodata.baju<<" ukuran celana saya "<<biodata.celana<<" ukuran sepatu saya "<<biodata.sepatu<<" tas saya adalah "<<biodata.tas<<endl;
}