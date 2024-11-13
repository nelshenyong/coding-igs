#include <iostream>
#include <array>
using namespace std;
//Syntax- Array:
// array < data_type, size > array_name;
int main()
{
    array < int, 5 > nilai;
    nilai[0] = 9;
    nilai[1] = 8;
    nilai[2] = 7;
    nilai[3] = 6;
    nilai[4] = 5;
    cout<<"Ke-0 Memory: "<<&nilai[0]<<" : "<<nilai[0]<< endl;
    cout << "-----------------------------"<<endl;
    for(int i = 0;i<5;i++){
        nilai[i] = i*2;
        cout<<"Ke-0 Memory: "<<&nilai[i]<<" : "<<nilai[i]<< endl;
    };
    cout << "-----------------------------"<<endl;
    cout<< "Memory awal : "<<nilai.begin() << endl;
    cout<< "Memory akhir : "<<nilai.end() << endl;
    cout << "Ke-4 dengan at: " << nilai.at(4) << endl;
    return 0;
}