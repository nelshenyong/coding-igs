#include <iostream> 
using namespace std;

int xyz = 10; //Variable Global 
double variable_global(){
    return xyz;
}
int main(){
    cout << "1. Variable Global = " << xyz << endl; //10

    int xyz = 11; //Variable Local
    cout << "2. Variable Local = " << xyz << endl; //11

    cout << "3. Variable Global = " << variable_global() << endl; //10

    // Scope Resolution ->          ::
    cout << "4. Variable Global = " << ::xyz << endl; //10

    {
        cout << "5. Variable Local = " << xyz << endl; //11
        int xyz = 12; //Variable Block
        cout << "6. Variable Block = " << xyz << endl; //12
    }

    cout << "7. Variable Local = " << xyz << endl; //11
}