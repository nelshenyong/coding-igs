#include <iostream>
using namespace std;
// array multidimensi :
void tampilArray(int *ptr, int baris, int kolom){
    int index = 0;
    for(int i = 0; i < baris; i++){
        cout<<"[ ";
        for(int j = 0; j < kolom; j++ ){
            cout<< *(ptr + index)<< " ";
            index += 1; //atau index++
        }cout<<"] "<< endl;
    }
}
int main()
{
//           baris kolom
    int nilai[ 2 ] [ 2 ] = { 9, 8, 7, 6};
    cout<< "baris 0 dan kolom 0 = "<<nilai[0][0] << endl;
    cout<< "baris 0 dan kolom 1 = "<<nilai[0][1] << endl;
    cout<< "baris 1 dan kolom 0 = "<<nilai[1][0] << endl;
    cout<< "baris 1 dan kolom 1 = "<<nilai[1][1] << endl;
    tampilArray(*nilai, 2, 2);
    return 0;
}