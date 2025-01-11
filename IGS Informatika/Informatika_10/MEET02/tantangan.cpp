#include <iostream>
using namespace std;
int main()
{
    int a,b,c,d,hasil1,hasil2,hasil3,hasil4;
    cout<<"Masukkan nilai a : ";
    cin>>a;

    cout<<"Masukkan nilai b : ";
    cin>>b;

    cout<<"Masukkan nilai c : ";
    cin>>c;

    cout<<"Masukkan nilai d : ";
    cin>>d;


    hasil1 = (a * b) - (c * d);
    cout<<"Hasil dari (a * b) - (c * d) adalah :"<<hasil1;
    hasil2 = (a * b) + (c * d);
    cout<<"Hasil dari (a * b) + (c * d) adalah :"<<hasil2;
    hasil3 = a % (b + c) * d * a;
    cout<<"Hasil dari a + b - a adalah :"<<hasil3;
}