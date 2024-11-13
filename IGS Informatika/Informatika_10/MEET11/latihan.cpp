#include <iostream>
using namespace std;
int main()
{
    int banyak, i, j;
    printf("Masukan angka: "); cin>>banyak;

    for (i = 1; i <= banyak; i += 1){
        printf("\n");
        printf("+ ");
        for (j = 1; j <= banyak; j += 1){
            printf("*");
        }
    }

    for (i = 1; i <= banyak; i += 1){
        printf("\n");
        printf("+ ");
        for (j = i; j <= banyak; j += 1){
            printf("*");
        }
    }
}