#include <iostream>
using namespace std;
// Syntax: arrayloop
// for(tipedata varloop: arrayname)sc

int main()
{
    int data[6] = {1, 2, 3, 4, 5, 6}
    for (int nilai : data)
    {
        nilai *= 10;
        cout << "Mmeory: " << &nilai << endl;
        cout << "Nilai: " << nilai << endl;
    }
    cout << "" << endl;
        for (int nilai : data)
    {
        cout << "Mmeory: " << &nilai << endl;
        cout << "Nilai: " << nilai << endl;
    }
    cout << "" << endl;
        for (int &nilai : data)
    {
        nilai *= 10; // akan merubah arrayq
        cout << "Mmeory: " << &nilai << endl;
        cout << "Nilai: " << &nilai << endl;
    }
    cout << "" << endl;
        for (int &nilai : data)
    {
        cout << "Mmeory: " << &nilai << endl;
        cout << "Nilai: " << &nilai << endl;
    }
    return 0;
}