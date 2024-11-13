#include <iostream>
#include <cstring>
using namespace std;
int main()
{
    char a[100], b[100];
    cout<<"Nama depan: ";
    cin>>a;
    cout<<"Nama belakang: ";
    cin>>b;

   cout<<"---------------------------------"<<endl;
   char*kata_gabung;
   strcat (a, " ");
   kata_gabung = strcat(a, b);
   cout<<"Kata gabung menjadi: "<<kata_gabung<<endl;

   cout<<"---------------------------------"<<endl;
   cout<<"Huruf akan menjadi kecil: "<<strlwr(kata_gabung)<<endl;
   cout<<"Huruf akan menjadi besar: "<<strupr(kata_gabung)<<endl;

   cout<<"---------------------------------"<<endl;
   cout<<"Jumlah str: "<<strlen(kata_gabung)<<endl;

   cout<<"---------------------------------"<<endl;
   cout<<"Kata akan terbalik: "<<strrev(kata_gabung)<<endl;
}