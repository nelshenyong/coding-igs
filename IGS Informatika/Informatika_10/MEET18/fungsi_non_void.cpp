#include <iostream>
using namespace std;
// Function non void - return
double Kali(int x, int y){
    return x * y;
}

void Kali(int x, int y){
    return x * y;
}

int main(){
    cout << "Hasil 5 x 125 = " << Kali(5, 125) << endl;
    int Hasil = Kali(5, 125) + 5;
    cout << "Hasil = " << Hasil << endl;
    // int hasil_1 = tambah(5, 2) + 5; Tidak bisa di operasikan
    // cout << "Hasil fungsi tambah (5, 2) = "<< tambah(5, 2);
    cout << "Hasil tambah(5, 2) = "; tambah(5, 2);
}
