#include <iostream>
using namespace std;

double Fib_rekursif(int num);

int main()
{
    cout << " fib ke 10 = " << Fib_rekursif(10)<<endl;
    cout << "deret fibronasi : "<<endl;
    for (int i = 1;i<=10 ;i++){
        cout << " fib ke-"<< i <<" = "<<Fib_rekursif(i)<<endl;
    }
    return 0;
}
double Fib_rekursif(int num){
    if(num== 0 || num==1 ){
        return num;
    }
    else {
        return Fib_rekursif( num -2 )+ Fib_rekursif ( num - 1);
    }
}