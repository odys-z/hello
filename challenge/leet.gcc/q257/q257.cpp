/**
 * 257. Binary Tree Paths
 * https://leetcode.com/problems/binary-tree-paths/
 */

#include <vector>
#include <string>
#include <iostream>
#include <numeric>

using namespace std;

/**
 * Definition for a binary tree node.
 */
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

/* 7ms */
class Solution {

public:
    void track(TreeNode* root, vector<vector<int>> &buf) {
        if (root == NULL) return;

        if (root->left == NULL and root->right == NULL) {
            buf.push_back(vector<int>{root->val});
            return;
        }
        else {
            vector<vector<int>> subtree;
			track(root->left, subtree);
			track(root->right, subtree);
            for (vector<int> &t : subtree)
                t.insert(t.begin(), root->val);

            buf.insert(buf.end(), subtree.begin(), subtree.end());
        }
    }

    vector<string> binaryTreePaths(TreeNode* root) {
        vector<vector<int>> res;
        track(root, res);

		auto join = [](string a, int e) {
			return move(a) + "->" + to_string(e);
		};

        vector<string> ss;
        for (vector<int> v : res)
            ss.push_back(accumulate(next(v.begin()), v.end(), to_string(v[0]), join));
        return ss;
    }
};

/* 6ms */
class Solution2 {
public:
    void dfs(TreeNode* root, vector<vector<int>>& sub, vector<int>& p) {
        p.push_back(root->val);
        if (root->left == NULL && root->right == NULL)
            sub.push_back(p);

        if (root->left != NULL) dfs(root->left, sub, p);
        if (root->right != NULL) dfs(root->right, sub, p);
    }

    vector<string> binaryTreePaths(TreeNode* root) {
        vector<vector<int>> res;
        vector<int> buf;
        dfs(root, res, buf);

        vector<string> ss;
        for (vector<int> v : res)
            ss.push_back(accumulate(next(v.begin()), v.end(), to_string(v[0]),
                [](string a, int e) { return move(a) + "->" + to_string(e); }));
        return ss;
    }
};

/* 0ms */
class Solution3 {
public:
    void dfs(TreeNode* root, vector<string>& sub, string p) {
        p += (p.length() == 0 ? "" : "->") + to_string(root->val);
        if (root->left == NULL && root->right == NULL)
            sub.push_back(p);

        if (root->left != NULL) dfs(root->left, sub, p);
        if (root->right != NULL) dfs(root->right, sub, p);
    }

    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> res;
        string buf = "";
        dfs(root, res, buf);

        return res;
    }
};



int main() {
    auto join = [](string a, string e) {
        return move(a) + ", " + e;
    };

    Solution3 s;
    TreeNode r = TreeNode(1, new TreeNode(2), new TreeNode(3));

    vector<string> v = s.binaryTreePaths(&r);
    cout << accumulate(next(v.begin()), v.end(), v[0], join) << endl;

    r = TreeNode(1, new TreeNode(2), new TreeNode(3, new TreeNode(4), NULL));
    v = s.binaryTreePaths(&r);
    cout << accumulate(next(v.begin()), v.end(), v[0], join) << endl;
}
