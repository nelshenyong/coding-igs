#include <iostream>
using namespace std;
// Fucntion: Pointer
void pangkatBiasa ( int b );
void pangkatBiasa ( int * );
int main()
{
    int a = 9;
    cout << "Addres memory a: " << &a << endl;
    cout << "Pangkat a: " << a << endl;
    cout << "-----------------------" << endl;
    pangkatBiasa(a);
    cout << "-----------------------" << endl;
    pangkatPointer(&a);
    return 0;
}
void pangkatBiasa ( int b ){
    cout << "Addres memory b: " << &b << endl;
    cout << "Pangkat b: " << b * b << endl;
}
void pangkatPointer ( int *c ) {
    cout << "Addres memory c: " << &c << endl;
    cout << "Pangkat c: " << (*c) * (*c) << endl;
}