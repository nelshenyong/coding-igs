#include <iostream>
using namespace std;
int main()
{
    string hari;
    cout<<"Opsi Pilihan\na) 1 = Senin\nb) 2 = selasa\nc) 3 = rabu\nd) 4 = kamis\ne) 5 = jum'at\nf) 6 = sabtu\ng) 7 = minggu\n";
    cout<<"Masukan Hari (1 - 7):  ";
    cin>>hari;
    cout<<"///////////////////////////////////////////\n";

    if(hari == "1")
    cout<<"Hari : Senin";

    else if(hari == "2")
    cout<<"Hari : Selasa";

    else if(hari == "3")
    cout<<"Hari : Rabu";

    else if(hari == "4")
    cout<<"Hari : Kamis";

    else if(hari == "5")
    cout<<"Hari : Jum'at";

    else if(hari == "6")
    cout<<"Hari : Sabtu";

    else if(hari == "7")
    cout<<"Hari : Minggu";

    else
    cout<<"Hari - hari bersamamu :)";
}