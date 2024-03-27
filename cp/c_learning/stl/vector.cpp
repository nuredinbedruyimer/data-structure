#include <bits/stdc++.h>

using namespace std;


int main(){
    vector<int> arr(1, 20);
  
    arr.push_back(17);
    arr.push_back(23);
    arr.push_back(43);
    arr.push_back(76);
      vector<int> brr(arr);
    vector<int> crr(arr.begin(), arr.end());
    cout<<"Last Element Removed or Popped : "<<arr.at(arr.size()- 1)<<endl;
    arr.pop_back();
    for (auto it: arr){
        cout<<it << " ";
    }
    cout<<endl;
        for (auto it: brr){
        cout<<it << " ";
    }
    cout<<endl;
        for (auto it: crr){
        cout<<it << " ";
    }

    // 2D array
    vector<int> arr1 = {1, 2, 3, 4};
    vector<int> arr2 = {1, 2, 3, 4, 7};
    vector<int> arr3 = {1, 2, 3, 4, 9, 19};

    vector<vector<int>> nestedVector;
    nestedVector.push_back(arr1);
    nestedVector.push_back(arr2);
    nestedVector.push_back(arr3);

    cout<<endl;

    cout<<"2d array here "<<endl;

    for (auto row: nestedVector){
        for (auto cell: row){
            cout<<cell<<" ";
        }
        cout<<endl;
    }

    vector<vector<int>> grid(4, vector<int>(4, 22));


        for (auto row: grid){
        for (auto cell: row){
            cout<<cell<<" ";
        }
        cout<<endl;
    }

    return 0;
    
}