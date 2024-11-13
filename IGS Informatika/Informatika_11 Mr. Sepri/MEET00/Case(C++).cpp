#include <iostream>
using namespace std;

void jenis_segitiga(int a, int b, int c){
    if(a == b && b == c){
        cout << "Segitiga sama sisi";
    } else if(a == b || a == c || b == c) {
        cout << "Segitiga sama kaki";
    } else if(a + b > c && a + c > b && b + c > a) {
        cout << "Segitiga sembarang";
    } else {
        cout << "Bukan segitiga";
    }
}

int main()
{
    int a,b,c;
    cout << "Masukkan panjang a: ";
    cin >> a;

    cout << "Masukkan panjang b: ";
    cin >> b;

    cout << "Masukkan panjang c: ";
    cin >> c;
    
    jenis_segitiga(a, b, c);

    return 0;
}