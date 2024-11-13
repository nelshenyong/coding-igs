#include <iostream> 
using namespace std;
// overloading Func.    
double persegi (int panjang, int lebar){
    int hasil_luas = panjang * lebar;
    return hasil_luas;
}

int persegi(int sisi){
int hasil_luas = sisi*sisi;
return hasil_luas;
    }

int main(){
    int p, l_s;
    cout << "Masukkan Panjang: "; cin >> p;
    cout << "\nMasukkan Lebar (sisi ): "; cin >> l_s;
    cout << "Luas persegi panjang = "<<persegi(p,l_s)<<endl;
    cout << "Luas persegi = "<<persegi(l_s)<<endl;
  

}