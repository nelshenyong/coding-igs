#include <iostream>
using namespace std;

int main()
{
    char kata1[50];
    unsigned char kata2[50];
    signed char kata3[50];
    string kata4;

cout<<"Masukkan kata 1: ";
//cin>>kata1;
cin.getline(kata1, 50);
cout<<"Value kata 1 adalah "<<kata1<<endl;

cout<<"Masukkan kata 2: ";
cin>>kata2;
cout<<"Value kata 2 adalah "<<kata2<<endl;

cout<<"Masukkan kata 3: ";
cin>>kata3;
cout<<"Value kata 3 adalah "<<kata3<<endl;

cout<<"Masukkan kata 4: ";
cin>>kata4;
cout<<"Value kata 3 adalah "<<kata4<<endl;
}