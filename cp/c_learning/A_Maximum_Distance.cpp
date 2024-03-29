#include <bits/stdc++.h>
using namespace std;
using vector_int = vector<int>;
using ll = long long;
using vector_pairs = vector<pair<int, int>>;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    ll length;
    cin >> length;

    vector_int xrr;
    xrr.resize(length);
    vector_int yrr;
    yrr.resize(length);

    vector_pairs points;

    for (int i = 0; i < length; i++){
        cin >> xrr[i];  
    }
    for (int i = 0; i < length; i++){
        cin>>yrr[i];
    }

    ll max_distance = -1;


    for (int i = 0; i < length; i++){
      points.push_back({xrr[i], yrr[i]});

    } 



    for (auto p1: points){
        for (auto p2: points){
            ll dist_x = (p1.first - p2.first) * (p1.first - p2.first);
            ll dist_y = (p1.second - p2.second) * (p1.second - p2.second);
            ll dist = dist_x + dist_y;
            
            max_distance =  max(dist, max_distance);




        }
    }
    cout<<max_distance ;
    
    return 0;
}
