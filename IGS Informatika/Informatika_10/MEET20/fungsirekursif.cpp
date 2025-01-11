#include <iostream> 
using namespace std;
// fungsi rekursif adalah fungsi yang akan menjalankan dirinya sendiri secara berulang (loops)
//comtoh func faktorial
double faktorial(int num){
    if (num > 1){
        return num *faktorial(num-1);    
    }
    else{
        return 1;
    }
}
int main(){
    int input_num;
    cout << "number : ";cin  >> input_num;
    cout << "faktorial : "<< input_num << " != " << faktorial(input_num) << endl;
}