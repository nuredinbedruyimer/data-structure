#include <bits/stdc++.h>
using namespace std;



int main(){
    array < int, 7> arr = {1, 2, 3, 4, 5, 6, 7};
    int total = 0;
    for (auto& element: arr){
        total += element;
    }
    int index =  1;
    //  or we can use iterator or traditional loop for more access of the place where we at
    cout<<"element at position "<< index << "Is " << arr.at(index) << endl;
    cout << "Sum Of The Array Become : " << total <<endl;

for (auto it = arr.begin(); it != arr.end(); ++it) {
    cout << *it << " ";
}
cout<<""<<endl;
// reverse traversing option 1
for (auto it = arr.end() - 1; it >= arr.begin();--it ){
    cout<<*it<<" ";
}
cout<<endl;
for(auto it: arr){
    cout << it << " ";
}

    return 0;

}