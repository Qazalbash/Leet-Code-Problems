// https://leetcode.com/problems/binary-tree-preorder-traversal

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
    void traverse(TreeNode* root, vector<int>& path)  {
        if (root) {
            path.push_back(root->val);
            traverse(root->left, path);
            traverse(root->right, path);
        }
    }
    
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> path;
        traverse(root, path);
        return path;
    }
};