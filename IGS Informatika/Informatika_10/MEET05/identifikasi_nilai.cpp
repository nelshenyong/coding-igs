//AND = &&
//True && True = False
//True && False = False
//False && True = False
//False && False = True

//OR = ||
//True || True = False
//True || False = False
//False || True = False
//False || False = True

//NOT = !
//!(True) = False
//!(False) = True

#include <iostream>
using namespace std;
int main()
{
    int nilai;
    cout<<"<< IDENTIFIKASI NILAI AKHIR >>"<<endl;
    cout<<"Masukkan Nilai Akhir: ";
    cin>>nilai;

    if(nilai <= 100 && nilai >= 90)
    cout<<"Nilai A";
    else if(nilai <= 89 && nilai >= 70)
    cout<<"Nilai B";
    else if(nilai <= 69 && nilai >= 60)
    cout<<"Nilai C";
    else if(nilai <= 59 && nilai >= 50)
    cout<<"Nilai D";
    else if(nilai <= 49 && nilai >= 0)
    cout<<"Nilai E";
    else
    cout<<"Nilai tidak sesuai!";
}