#include <iostream>
using namespace std;
int main()
{
    int x,y,z,hasil1,hasil2;
    cout<<"Masukkan nilai x : ";
    cin>>x;

    cout<<"Masukkan nilai y : ";
    cin>>y;

    cout<<"Masukkan nilai z : ";
    cin>>z;


    hasil1 = (x + y) - (x / y) * y / z;
    cout<<"Hasil dari ((x + y) - (x / y) * y / z) adalah :"<<hasil1<<endl;
    hasil2 = (x - y) + (x * y) * y - z;
    cout<<"Hasil dari ((x - y) + (x * y) * y - z) adalah :"<<hasil2;
}