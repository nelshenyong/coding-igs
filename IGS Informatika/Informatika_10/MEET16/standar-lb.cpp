#include <iostream>
#include <cmath>
#include <cstdlib>
using namespace std;
int main(){
    cout << "5 pangkat 8 = " << pow(5,8) << endl;
    cout << "2 pangkat 4 = " << pow(2,4) << endl;
    cout << "akar dari 256 = " << sqrt(256) << endl;
    cout << "akar dari 729 = " << sqrt(729) << endl;
    cout << "akar dari 16 = " << sqrt(16) << endl;
    cout << "Random = " << rand() << endl;

    cout << "\n";
    for (int i = 0; i < 4; i++){
    cout << "New Random = " << rand() << endl;

    }
}