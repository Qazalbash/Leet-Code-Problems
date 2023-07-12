// https://leetcode.com/problems/reverse-nodes-in-k-group

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
    ListNode* reverseKGroup(ListNode* head, int k) {
        stack<int> s;
        ListNode* node = new ListNode();
        ListNode* new_head = node;
        ListNode* prev;
        while (head) {
            int i = 0;
            while(head && i < k) {
                s.push(head->val);
                head = head->next;
                ++i;
            }
            while (i == k && s.size()) {
                node->val = s.top();
                s.pop();
                node->next = new ListNode();
                prev = node;
                node = node->next;
            }
        }
        if (!s.empty()) {
            stack<int> inv_s;
            while(!s.empty()) {
                inv_s.push(s.top());
                s.pop();
            }
            while (inv_s.size()) {
                node->val = inv_s.top();
                // cout << s.top() << endl;
                inv_s.pop();
                node->next = new ListNode();
                prev = node;
                node = node->next;
            }
        }
        prev->next = nullptr;
        return new_head;
    }
};