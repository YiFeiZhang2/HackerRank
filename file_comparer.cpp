#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <iterator>
using namespace std;

int main(int argc, char* argv[]){

    if ( argc != 3){
        cout << "wrong number of arguments" << endl;
        return -1;
    }

    std::ifstream fileA(argv[1]);
    std::ifstream fileB(argv[2]);

    if (!fileA.is_open())
        cout << "could not open first file" << endl;
    if (!fileB.is_open())
        cout << "could not open second fle" << endl;

    std::string A;
    std::string B;
    int lineNum = 1;
    int total = 0;

    while (fileA >> A && fileB >> B){
        if (A != B)
            cout << lineNum << endl;
        else
            total += 1;
        ++lineNum;
    }
    cout << total << endl;
    return 0;
}