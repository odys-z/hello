
#include <string>
#include <vector>
#include <sstream>
#include <iostream>

using namespace std;

class Solution {
public:
    string smallestNumber(string pattern) {
        vector<char> stack;
        stringstream reslt;

        for (int x = 0; x <= pattern.length(); x++) {
            stack.push_back(0x30+x+1);
            if (x == pattern.length() || pattern.at(x) == 'I')
                while (stack.size() > 0) {
                    reslt << stack.back();
                    stack.pop_back();
                }
        }
        return reslt.str();
    }
};

int main() {
    Solution s;
	cout << endl << s.smallestNumber("IIIDIDDD") << endl;
    return 0;
}