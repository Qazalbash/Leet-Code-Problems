// https://leetcode.com/problems/remove-linked-list-elements

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode* node = head;
        while (node) {
            if (node->next && node->next->val == val) {
                node->next = node->next->next;
            }
            else {
                node = node->next;
            }
        }
        if(head && head->val==val){
            return head->next;
        }
        return head;
    }
};