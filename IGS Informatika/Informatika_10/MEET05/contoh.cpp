#include <iostream>
using namespace std;
int main()
{
    int umur;
    cout<<"<< IDENTIFIKASI KTP >>"<<endl;
    cout<<"Masukkan usia:";
    cin>>umur;
    if(umur >= 17)
    cout<<"Berhak membuat KTP";
    else
    cout<<"Tidak berhak membuat KTP";
}