#include <iostream>
#include <array>    
using namespace std;

int main()
{
    array < array < int, 2>, 2 > nilai = {9, 8, 7, 6};
    cout<< "baris 0 dan kolom 0 = "<<nilai[0][0]<<endl;
    cout<< "baris 0 dan kolom 1 = "<<nilai[0][1]<<endl;
    cout<< "baris 1 dan kolom 0 = "<<nilai[1][0]<<endl;
    cout<< "baris 1 dan kolom 1 = "<<nilai[1][1]<<endl;
    return 0;
}