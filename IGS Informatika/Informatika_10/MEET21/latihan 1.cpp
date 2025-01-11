#include <iostream> 
using namespace std;

string nama = "Nelshen Yong"; //Variasi GLobal
string agama = "Buddha"; // Variabel Global
int kelas = 10; // Variasi Global

int main(){ 
    cout << "----- Global - Local - Block -----" << endl;
    cout << "Nama: " << nama << endl; 
    cout << "Agama: " << agama << endl; 
    cout << "Kelas: " << kelas << endl; 

    string ttl = "25 September 2008"; // Variabel Local
    cout << "Tanggal lahir: " << ttl << endl; 

    {
        int tinggi =  178; // Variabel Local di Block
        string alamat = "Palembang, Sumatera Selatan, Indonesia 30152"; // Variabel Local di Block
        cout << "Tinggi badan : " << tinggi << endl; 
        cout << "Alamat : " << alamat << endl; 

    }
}