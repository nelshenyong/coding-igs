#include <iostream>
using namespace std;
// Reference: Statement yang digunakan sebagai alias / initial / nama lain dari variabel.

int main()
{
    int a = 10;
    cout << "Value a: " << a << endl;
    cout << "Address a: " << &a << endl;
    cout << "--------------" << endl;
    int b = a;
    cout << "Value b: " << b << endl;
    cout << "Address b: " << &b << endl;
    b = 12;
    cout << "New Value a: " << a << endl;
    cout << "--------------" << endl;

    // Reference
    int &c = a;
    cout << "Value c: " << c << endl;
    cout << "Address c: " << &c << endl;
    cout << "--------------" << endl;
    c = 46;
    cout << "New Value a: " << a << endl;
    return 0;
}


