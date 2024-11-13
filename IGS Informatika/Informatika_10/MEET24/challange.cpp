#include <iostream>
#include <array>
using namespace std;

int main()
{
    array<array<string, 5>, 3> nilai = {
        "jeje", "", "", "", "",
        "x.10", "", "", "infor", "",
        "mail@oktvk.com", "", "", "", "md"
    };

    cout << "baris 0 kolom 0, value = " << nilai[0][0] << endl;
    cout << "baris 1 kolom 0, value = " << nilai[1][0] << endl;
    cout << "baris 2 kolom 0, value = " << nilai[2][0] << endl;
    cout << "baris 1 kolom 3, value = " << nilai[1][3] << endl;
    cout << "baris 2 kolom 4, value = " << nilai[2][4] << endl;

    return 0;
}