#include <iostream>
#include <conio.h>
using namespace std;
int main(){
    int bil;
    back:
        system ("cls");
        printf("Masukan angka : ");cin>>bil;
        printf( "hasil dari %i % 2 = %i",bil,bil%2);
        char lagi;
        printf("\nLanjut (y/t) : ");cin>>lagi;
        if (lagi == 'y' ||lagi=='Y'){
            goto back;
        }














}