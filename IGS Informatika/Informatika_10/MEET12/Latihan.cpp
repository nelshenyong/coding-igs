#include <iostream>
#include <conio.h>
using namespace std;
int main(){
    int i,angka;
    int banyak_bagi = 0 :
    char lagi;

    back:
        system("cls");
        printf("__________IDENTIFIKASI BIL KOMPOSIT__________/n")
        printf("Masukan angka : ");cin>>angka;
        for (i =1;i<=angka;i++){
            if (angka%i==0){
                banyak_bagi += 1;
            }

        }
        if(banyak_bagi>2){
            printf("\n %i BILANGAN KOMPOSIT",angka)
        }
        else{
            printf("\n %i BILANGAN BUKAN KOMPOSIT",angka)
        }
        printf("lanjutkan (Y/T) : ");cin>>lagi;
        if (lagi=='y')





}        