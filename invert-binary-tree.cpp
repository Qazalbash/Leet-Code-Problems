// https://leetcode.com/problems/invert-binary-tree

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
    TreeNode* invertTree(TreeNode* root) {
        if (!root) return NULL;
        TreeNode* left = root->left;
        TreeNode* right = root->right;
        if (left && !right) {
            root->right = new TreeNode(left->val, left->left, left->right);
            invertTree(root->right);
            root->left = nullptr;
        }
        if (right && !left) {
            root->left = new TreeNode(right->val, right->left, right->right);;
            invertTree(root->left);
            root->right = nullptr;
        } 
        if (left && right) {
            root->right = new TreeNode(left->val, left->left, left->right);
            invertTree(root->right);
            root->left = new TreeNode(right->val, right->left, right->right);;
            invertTree(root->left);
        } 
        return root;
    }
};