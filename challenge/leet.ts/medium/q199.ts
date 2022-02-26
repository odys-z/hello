/**
 * Definition for a binary tree node.
 */
class TreeNode {
    val: number
    left: TreeNode | null
    right: TreeNode | null
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.left = (left===undefined ? null : left)
        this.right = (right===undefined ? null : right)
    }
}

/**
 * 49.04%
 * @param root 
 * @returns 
 */
function rightSideView(root: TreeNode | null): number[] {
    if (TreeNode == null) return [];
    
    let q = [root];
    let q_ = [] as TreeNode[];
    let rview = [] as number[];
    
    while(q.length > 0) {
        rview.push(q[q.length - 1].val);

        for (let n of q) {
            if (n.left !== null)
                q_.push(n.left);
            if (n.right !== null)
                q_.push(n.right);
        }

        q = q_;
    }
    
    return rview;
};