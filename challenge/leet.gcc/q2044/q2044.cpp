#include <iostream>
#include <vector>
#include <set>
#include <unordered_map>

using namespace std;

class Solution {
    void printvect(vector<int>& v) {
        cout << endl;
        for (int e : v) {
            cout << e << ", ";
        }
    }

    int maxor = 0;
    int rescnt = 0;

public:
    int ors (vector<int> &nums) {
        int r = 0;
        for (int n : nums) r |= n;
        return r;
    }

    void countMaxor(vector<int>& nums, int start, int startor, vector<int>& orstack, vector<int>& buf) {
        if (startor == this->maxor) {
            printvect(buf);
            this->rescnt++;
        }

        if (start >= nums.size()) return;

        int ori = startor;
        for (int i = start; i < nums.size(); i++) {
            ori |= nums.at(i);
            orstack.push_back(ori);

			buf.push_back(nums.at(i));
			countMaxor(nums, i+1, ori, orstack, buf);

			buf.pop_back();
            orstack.pop_back();
            ori = orstack.back();
        }
    }

    int countMaxOrSubsets(vector<int>& nums) {
        for (int n : nums) {
            maxor |= n;
        }

        vector<int> buf;
        vector<int> orstack{ 0 };
        countMaxor(nums, 0, 0, orstack, buf);

        return this->rescnt;
    }
};

class Solution2 {
public:
    static int countMaxOrSubsets(const std::vector<int>& nums) {
        int maxOr = 0;
        unordered_map<int, int> counter{ {0, 1} };
        for (auto a : nums) {
            auto next = counter;
            for (const auto& p : counter) {
                next[p.first | a] += p.second;
            }
            counter = next;
            maxOr |= a;
        }
        return counter[maxOr];
    }
};

int main()
{
    Solution2 s;
    vector<int> nums{ 3, 5, 1, 2 };
    for (int q : nums) {
		cout << q << " - ";
    }
	cout << endl << s.countMaxOrSubsets(nums) << endl << endl;

    return 0;
}
