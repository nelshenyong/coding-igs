#include <iostream>
using namespace std;
int main(){
    int bulan;

cout<<">> IDENTIFIKASI BULAN <<";
cout<<"1. Januari \n2. Februari\n3. Maret \n4. April \n5. Mei \n6. Juni \n7. Juli \n8. Agustus \n9.September \n10. Oktober \n11. November \n12. Desember \n";
cout<<"------------------------------- \n";

cout<<"\n Masukan Pilihan (1 - 12): \n";
cin>>bulan;

switch (bulan)
{
case 1:
    cout<<"\nBulan Januari";
    break;

case 2:
    cout<<"\nBulan Februari";
    break;

case 3:
    cout<<"\nBulan Maret";
    break;

case 4:
    cout<<"\nBulan April";
    break;

case 5:
    cout<<"\nBulan Mei";
    break;

case 6:
    cout<<"\nBulan Juni";
    break;

case 7:
    cout<<"\nBulan Juli";
    break;

case 8:
    cout<<"\nBulan Agustus";
    break;

case 9:
    cout<<"\nBulan September";
    break;

case 10:
    cout<<"\nBulan Oktober";
    break;

case 11:
    cout<<"\nBulan November";
    break;

case 12:
    cout<<"\nBulan Desember";
    break;
 
}

}