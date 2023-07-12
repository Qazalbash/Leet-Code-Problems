// https://leetcode.com/problems/path-sum

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool hasPathSum(TreeNode* root, int targetSum, bool found = false) {  
        if (root == nullptr) {
            return false;
        }

        bool left = false, right = false;

        if (root->left) {
            root->left->val += root->val;
            left |= hasPathSum(root->left, targetSum);
        }

        if (root->right) {
            root->right->val += root->val;
            right |= hasPathSum(root->right, targetSum);
        }

        if (root->val == targetSum && root->left == nullptr && root->right == nullptr) {
            return true;
        }

        return left || right;
    }
};