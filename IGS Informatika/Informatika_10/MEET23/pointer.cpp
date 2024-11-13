#include <iostream>
using namespace std;
//Pointer: Variable khusus, yang berisi address memory.
//Ram: (Random Access Memory) Berfungsi sebagai penyimpanan sementara.
int main()
{
    int abc = 85;
    double xyz = 101;
    cout << "Value abc: " << abc << endl;
    cout << "Address memory abc: " << &abc << endl;
    cout << "Value xyz: " << xyz << endl;
    cout << "Address memory xyz: " << &xyz << endl;

    // Variable pointer: 
    int *ptr = &abc;
    cout << "Address memory ptr: " << *ptr << endl;
    *ptr = 777;
    cout << "Value abc: " << abc << endl;
    cout << "Value ptr: " << *ptr << endl;

    return 0;
}