#include <iostream>
using namespace std;
int main()
{
    int x;
    cout<<"<<< IDENTIFIKASI BILANGAN GENAP GANJIL>>>"<<endl;

    cout<<"Masukkan nilai X: ";
    cin>>x;
    
    if(x % 2 == 0)
    cout<<"Genap"<<endl;
    
    else if(x % 2 == 1)
    cout<<"Ganjil";
}