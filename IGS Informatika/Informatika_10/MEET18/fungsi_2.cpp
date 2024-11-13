#include <iostream>
using namespace std;
double rumusku( int x ,int y){
    int hasil = 3 * (x + y) - x + 1;
    return hasil;
}

void tampil(double hasil){
    cout << "Hasil 3 (x + y) - x + 1 = "<< hasil;
}

int main(){
    int x_1, y_1;
    cout << "Nilai x = "; cin >> x_1;
    cout << "Nilai y = "; cin >> y_1;
    tampil(rumusku(x_1, y_1));
}