#include <bits/stdc++.h>
using namespace std;
using vector_int = vector<int>;
using ll = long long;


int main(){

    int test;

    cin>> test;

    while (test--){
    int n;
    cin>>n;
    vector_int arr(n);
    vector_int brr(n);
    for (int i=0; i < n; i++){
        cin>>arr[i];
    }

        for (int i=0; i < n; i++){
        cin>>brr[i];
    }

    int count = 0;


    for (int i = 0; i < n; i++){
        if (arr[i] < brr[i]){
            count ++;

        }
    }
    if(count >= 2){
        cout<<"NO"<<endl;
    }
    else if(count == 0){
        cout<<"YES"<<endl;
    }
    else{
        int min_have = INT_MAX;
        int min_need = 0;
          for (int i = 0; i < n; i++){ 
            if (arr[i] < brr[i]){
                min_need = brr[i] - arr[i];
            }
            else if( arr[i] >= brr[i]){
                min_have = min(min_have, arr[i] - brr[i]);
            }

    }
    if(min_need > min_have){
        cout<<"NO"<<endl;
    }
    else{
        cout<<"YES"<<endl;
    }


    }




}}
