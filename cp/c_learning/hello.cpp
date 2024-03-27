#include <iostream>
#include <bits/stdc++.h>
using namespace std;

struct node{
    int index;
    double weight;
    bool isRemoved;
    string name;

    node(int index, double weight,bool isRemoved, string name){
       this -> index = index;
       this -> weight = weight;
       this -> isRemoved = isRemoved;
       this -> name = name;
    }
};

int main() {
    cout << "Hello, World from C++!" << endl;
    int age = 12;
    double height = 123.3;
    node n =   node(12, 12.2, true, "Abebe");
    cout<<"Height And Age Product Become : " << n.index <<endl;
    

    return 0;
}