#include <iostream> 
using namespace std;
#include <cmath>
#include <cstdlib>

void penjumlahan(int a, int b){
    cout << a << " + " << b << " = " << a+b << endl;
}
void pengurangan(int a, int b){
    cout << a << " - " << b << " = " << a-b << endl;
}
void perkalian(int a, int b){
    cout << a << " x " << b << " = " << a*b << endl;
}
void pembagian(int a, int b){
    cout << a << " / " << b << " = " << a/b << endl;
}
void akar(int a){
    cout << a << " akar " << " = " << sqrt(a) << endl;
}
void pangkat(int a, int b){
    cout << a << " pangkat " << b << " = " << pow(a, b) << endl;
}

int main(){
    penjumlahan(1, 2);
    pengurangan(1, 2);
    perkalian(1, 2);
    pembagian(1, 2);
    akar(4);
    pangkat(1, 2);

}