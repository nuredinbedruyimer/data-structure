#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int test;
    cin >> test;

    while (test--) {
        int n, m, k;
        cin >> n >> m >> k;
        
        vector<int> mrr(m), krr(k);
        
        // Read mrr and krr arrays
        for (int i = 0; i < m; ++i) {
            cin >> mrr[i];
        }
        for (int i = 0; i < k; ++i) {
            cin >> krr[i];
        }

        // Prepare all_questions and unknown_question vectors
        vector<int> allQuestions;
        for (int i = 1; i <= n; ++i) {
            allQuestions.push_back(i);
        }

        vector<int> unknownQuestion;
        for (int question : allQuestions) {
            if (find(krr.begin(), krr.end(), question) == krr.end()) {
                unknownQuestion.push_back(question);
            }
        }

        // Case one
        string ans = "";
        if (unknownQuestion.size() >= 2) {
            ans = string(m, '0');
        } else if (unknownQuestion.size() == 0) {
            ans = string(m, '1');
        } else {
            for (int ques : allQuestions) {
                if (ques == unknownQuestion[0]) {
                    ans += "1";
                } else {
                    ans += "0";
                }
            }
        }
        cout << ans << endl;
    }

    return 0;
}
