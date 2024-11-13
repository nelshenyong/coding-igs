#include <iostream>
using namespace std;
// Konstata / const : variabel yang tidak bisa diubah valuenya 
// dengan 2 cara: 
// 1. Define 
// 2. Const
#define PANJANG 10;
#define LEBAR 7; 
int main()
{
    int a = 10;
    cout << "Panjang = " << PANJANG;
    cout << "\nLebar = " << LEBAR;
    cout << "\nHasil = " << PANJANG * LEBAR;
    cout << "\na * b = " << a * b;
    // a = 40; // tidak bisa diubah !
    return 0;
}