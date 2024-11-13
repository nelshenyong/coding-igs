#include <iostream>
using namespace std;

string nama = "Kodok";

int main(){
    cout << "1. Variable Global = " << ::nama << endl;

    string nama = "Asep"; //Variable Local
    int umur = 11; //Variable Local
    cout << "2. Variable Local = " << nama << endl; 
    cout << "3. Variable Local = " << umur << endl; 

    {
        string nama = "Yanto";
        string cita_cita = "Pengamen";
        cout << "4. Variable Block = " << nama << endl; 
        cout << "5. Variable Block = " << cita_cita << endl; 
    }
}