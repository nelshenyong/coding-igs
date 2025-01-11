#include <iostream>
using namespace std;
int main(){

int x, y;
float hasil, jumlah;

cout<<"Masukan nilai:";
cin>>y;

jumlah = 0;

for ( x = 1; x <= y; x++){

jumlah+=x;
hasil = jumlah / y;

cout<<"------------------------\n";
cout<< "Urutan: "<<x<<"\n";
cout<< "Jumlah data: " <<jumlah<<"\n";
cout<< "Mean: " <<hasil<<"\n";

}
}