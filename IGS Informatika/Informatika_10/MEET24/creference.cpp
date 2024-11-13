#include <iostream>
using namespace std;
//Function : variable Parameter, v.refrence 
void fungsi (int &);
int main()
{
    int a = 6;
    cout<< " value a = "<< a <<endl;
    cout<< "Address memory a = "<< endl;
    fungsi(a);
    return 0;
}
void fungsi (int &nilaiREF){
    nilaiREF = 77;
    cout<< "Value nilaiRef = "<< nilaiREF << endl;
    cout<< "Address Memory NilaiRef : "<< &nilaiREF<<endl;
    cout<< " Kuadrat Memory NilaiRef : "<< &nilaiREF<<endl;
}
int kuadrat (int &angka){
	angka = angka * angka;
	return angka;
}