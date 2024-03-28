#include <bits/stdc++.h>

using namespace std;


int main(){
    vector<float> prices = {12.2, 34, 43.4, 45, 65.5};


    float totalPrice = 0;
    int lastIndex = 0;

    for (auto price: prices){
        cout<<" current Price Is : "<< price << endl;
        totalPrice += price;
        lastIndex += 1; 

    }

    cout<<" total Price Also Become : " << totalPrice<<endl;

    //  Let us Add new 5 days price to the vector

    prices.push_back(233.3);
    prices.push_back(23.3);
    prices.push_back(323.3);
    prices.push_back(324.44);
    prices.push_back(5.3);



    for (int index = lastIndex; index < prices.size(); index++){
        cout<<"Added Price : " << prices[index] << endl;


    }

    //  insert elemenr at front end and random point

    prices.insert(prices.begin(), 10000);
    prices.insert(prices.end(), 87000);

    prices.insert(prices.begin() + 3, 9686);

    cout<< prices[0] << prices[prices.size() - 1] << prices[3] << endl;


    prices.erase(prices.begin(), prices.begin() + 7);
    cout<< prices.size() << endl;

    int intialValue = 10;
    int rows = 3;
    int columns = 4;


    vector<vector<int>> grid(rows, vector(columns, intialValue));


    for (auto row : grid){
        for (auto cell : row){
            cout<<"cell : (" <<cell << ")" << endl; 
        }
    }


    

    


    return 0;
}