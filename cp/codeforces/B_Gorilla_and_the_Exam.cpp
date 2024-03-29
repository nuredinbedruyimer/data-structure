#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int main() {
    int test;
    cin >> test;

    for (int t = 0; t < test; ++t) {
        int n, k;
        cin >> n >> k;
        
        vector<int> arr(n);
        for (int i = 0; i < n; ++i) {
            cin >> arr[i];
        }

        map<int, int> memo;
        for (int a : arr) {
            memo[a]++;
        }

        vector<int> brr;
        for (auto& pair : memo) {
            brr.push_back(pair.second);
        }

        sort(brr.begin(), brr.end());

        int curr_sum = 0;
        int ans = brr.size();

        for (int index = 0; index < brr.size(); ++index) {
            int curr = brr[index];

            if (k >= curr && index != n - 1) {
                ans--;
                k -= curr;
            } else {
                break;
            }
        }

        cout << max(ans, 1) << endl;
    }

    return 0;
}
