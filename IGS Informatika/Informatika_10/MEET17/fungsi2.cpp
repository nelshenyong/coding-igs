#include <iostream>
using namespace std;

//Funtion dengan parameter
void MyName(string name){
    cout << "Nama Saya " << name << endl;
    } // name
void MyClass (string kelas, string jurusan){
    cout << "Kelas Saya " << kelas << " Pada Jurusan " << jurusan << endl;
}
void smpku(string smp = "SMP Tinus"){
    cout << "SMP saya di " << smp << endl;
}
int main(){
    MyName("Bunga");
    MyClass("X.10", "Informatika");
    smpku();
}