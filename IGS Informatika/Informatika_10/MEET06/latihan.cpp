#include <iostream>
using namespace std;
int main()
{
    string username, password;
    cout<<"<< LOGIN >>"<<endl;
    cout<<"Username: ";
    cin>>username;
    cout<<"Password: ";
    cin>>password;

    string userKey, passKey;
    userKey = "user";
    passKey = "admin123";

    if(username == userKey && password == passKey)
    cout<<"Login Berhasil!";

    else if(username == userKey || password == passKey)
    cout<<"Username atau Password salah!";
    else
    cout<<"Login gagal!";
}