#include <iostream>
#include <vector>

using namespace std;

/* Definition for a binary tree node. */
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> buff;
        vector<TreeNode*> edge = {root};
        bsf(edge, buff);
        return buff;
    }

    vector<vector<int>> bsf(vector<TreeNode*> edge, vector<vector<int>> &collect) {
        vector<int> back;
        vector<TreeNode*> border = {};
        for (TreeNode* e : edge) {
            if (e != NULL) {
                back.push_back(e->val);
                border.push_back(e->left);
                border.push_back(e->right);
            }
        }
        if (back.size() > 0) {
            collect.push_back(back);
            bsf(border, collect);
        }
        return collect;
    }
};

class Solution2 {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> coll;
        if (root == NULL) return coll;

        vector<TreeNode*> edge {root};

        while(edge.size() > 0) {
            vector<int> buf {};
            vector<TreeNode*> edg_;
            for (TreeNode* np : edge) {
                if (np->left != NULL)
                    edg_.push_back(np->left);
                if (np->right != NULL)
                    edg_.push_back(np->right);
                buf.push_back(np->val);
            }

            coll.push_back(buf);
            edge = edg_;
        }
        return coll;
    }
};

int main()
{
    // [3,9,20,null,null,15,7]
    TreeNode* lch  = new TreeNode(9);
    TreeNode* rlch = new TreeNode(15);
    TreeNode* rrch = new TreeNode(7);
    TreeNode* rch  = new TreeNode(20, rlch, rrch);
    TreeNode* root = new TreeNode(3, lch, rch);

    Solution2* s = new Solution2();

    bool r0 = true;
    for (vector<int> &lvel : s->levelOrder(root)) {
        if (!r0) cout << ",";
        else r0 = false;
        cout << "[";
        bool e0 = true;
        for (int i : lvel) {
            if (!e0) cout << ",";
            else e0 = false;
            cout << i;
        }
        cout << "]";
    }

    cout << endl;
    return 0;
}

