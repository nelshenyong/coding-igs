#include <iostream>
#include <string>
using namespace std;

int main() {
    string multi_dim_array[3][2] = {
        {"r", "Bahasa"},
        {"Pemograman", "r"},
        {"r", "C++"}
    };

    cout << "Salah satu " << multi_dim_array[0][1] << " dalam " << multi_dim_array[1][0] << " adalah " << multi_dim_array[2][1] << endl;

    return 0;
}
