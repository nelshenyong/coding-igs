#include <iostream>
using namespace std;
int main() {
    float angka;
    cout << "Masukkan angka: ";
    cin >> angka;
    int jumlah = 0;
    int min = 1;
    int max = 0;
    for (float i = 1; i <= angka; i++) {
        jumlah += i;
        if (i < min) {
            min = i;
        }
        if (i > max) {
            max = i;
        }
    }
    cout << "Jumlah dari 1 hingga " << angka << " adalah " << jumlah << endl;
    cout << "Mean: " << (jumlah / angka) << endl;
    cout << "Angka minimal: " << min << endl;
    cout << "Angka maksimal: " << max << endl;
    return 0;
}