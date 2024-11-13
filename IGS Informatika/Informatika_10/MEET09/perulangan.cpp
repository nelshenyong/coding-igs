#include <iostream>
using namespace std;
int main(){
    int x, y;

for ( x = 1; x <= 10; x++ ){
cout<< x <<" ";
}

cout<<"\n------------------\n";
for (x = 1; x <= 10; x += 1){
    cout<< x << " ";
}

cout<<"\n------------------\n";
for (x = 10; x >= 1; x--){
    cout<< x << " ";
}

cout<<"\n------------------\n";
for ( x = 10; x >= 1; x -= 1){
    cout<< x << " ";
}

cout<<"\n1. Ganjil-----------------\n";
for ( x = 1; x <= 10; x += 2){
    cout<< x << " ";
}

cout<<"\n2. Ganjil-----------------\n";
for ( x = 1; x <= 10; x++){
    if (x % 2 == 1 ){
        cout<< x << " ";
    }
}

cout<<"\n1. For nested-----------------\n";
for ( x=1; x <=5; x++){
    cout<<"x = " <<x<< endl;
    for (y=1; y <=2; y++){
      cout<<"y = " <<y;
 }
}

}

