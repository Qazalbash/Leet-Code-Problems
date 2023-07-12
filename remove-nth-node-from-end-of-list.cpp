// https://leetcode.com/problems/remove-nth-node-from-end-of-list

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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if(head == nullptr || head->next == nullptr ) return nullptr;
        
        ListNode* node = head;
        int size = 0;
        
        while(node) {
            node = node->next;
            ++size;
        }

        if(size == n) {
            head = head->next;
            return head;
        }
        
        node = head;
        ListNode* temp = head;
        
        for(int i=0; i + n < size; ++i) {
            node = temp;
            temp = temp->next;
        }

        node->next = temp->next;

        return head;
    }
};