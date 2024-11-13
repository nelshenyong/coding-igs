#include <iostream>
using namespace std;
// Array: struktur data yang digunakan untuk menyimpan sekumpulan data dengan tipe yang sama
// Array memiliki panjang yang tetap
// Array memiliki index yang dimulai dari 0
// Contohnya:
// 0='2' 1='5' 2='10' 3='0' ...n
int main()
{
    int nilai [4];
    nilai[0] = 2;
    nilai[1] = 5;
    nilai[2] = 10;
    nilai[3] = 0;
    cout << "Address memory ke-0 " << &nilai[0] << " : " << nilai[0] << endl;
    return 0;
}