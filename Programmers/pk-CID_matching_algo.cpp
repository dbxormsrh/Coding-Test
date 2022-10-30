#include <iostream>
#include <string>

using namespace std;

int main(){
    string a = "2022-10-13_16:19:24.788";
    string b = "2022-10-13_16:19:24.572";

    if(a>b)
        cout << "a > b" << endl;
    else
        cout << "a < b" << endl;
}