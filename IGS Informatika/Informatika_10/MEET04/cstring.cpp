#include <iostream>
#include <cstring>
using namespace std;

int main()
{
   //STRCPY
   char kata1[] = "Pertama";
   char kata2[] = "Kedua";
   strcpy(kata1, kata2);
   cout<<"Kata 1 berisi: "<<kata1<<endl;

   cout<<"---------------------------------"<<endl;
   //STRNCPY
   char kata3[] = "Ketiga";
   char kata4[] = "Keempat";
   strncpy(kata3,kata4,4);
   cout<<"Kata 3 akan disalin sebanyak N kata4 "<<kata3<<endl;

   cout<<"---------------------------------"<<endl;
   //STRDRUP
   char kata5[] = "INI KATA 5!";
   char*kata6;
   kata6 = strdup(kata5);
   cout<<"Kata 6 menjadi value kata 5: "<<kata6<<endl;

   cout<<"---------------------------------"<<endl;
   //STRCAT
   char kata7[] = "Ketujuh";
   char kata8[] = "Kedelapan";
   char*kata_gabung;
   strcat (kata7, " ");
   kata_gabung = strcat(kata7, kata8);
   cout<<"Kata gabung menjadi: "<<kata_gabung<<endl;

   cout<<"---------------------------------"<<endl;
   //STRNCAT
   char kata9[] = "Meja";
   char kata10[] = "Kursi";
   char*kata_gabung_n;
   kata_gabung_n = strncat(kata9,kata10,3);
   cout<<"Kata gabung sebanyak N: "<<kata_gabung_n<<endl;

   cout<<"---------------------------------"<<endl;
   //STRLEN
   char kata11[] = "Siapa suruh sekolah di IGS";
   cout<<"Jumlah str di Kata 11: "<<strlen(kata11)<<endl;

   cout<<"---------------------------------"<<endl;
   //STRREV
   cout<<"Kata 11 akan terbalik: "<<strrev(kata11)<<endl;

   cout<<"---------------------------------"<<endl;
   //STRCHR
   char kata12[] = "Aku mw jugah";
   cout<<"Hasil dari str dengan awal J di kata: "<<strchr(kata12,'j')<<endl;

   cout<<"---------------------------------"<<endl;
   //STRLWR & STRUPR
   char kata13[] = "INI ADALAH HURUF BESAR";
   char kata14[] = "INI ADALAH HURUF KECIL";

   cout<<"Huruf akan menjadi kecil: "<<strlwr(kata13)<<endl;
   cout<<"Huruf akan menjadi besar: "<<strupr(kata14)<<endl;
}