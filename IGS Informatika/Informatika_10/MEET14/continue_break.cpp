#include <iostream>
using namespace std;
int main(){

//Statement Break
int i;
for (int i = 1; i <= 6; i += 1) {
        cout << i << endl;
    if(i == 4){
        break;
    }
    }

/////////////
cout<<"\n\n";
/////////////

//Statement Continue
int x;
x = 1;
while(x <= 6){
    if (x == 2){x++; continue;}
    cout<<x<<endl;
    x++;
}
}