// https://leetcode.com/problems/merge-k-sorted-lists

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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        const int size = lists.size();
        if (size == 0) return NULL;
        vector<int> m;
        int i;
        
        for(i = 0; i < size; ++i) {
            ListNode* k_head = lists[i];
            while (k_head!=nullptr) {
                m.push_back(k_head->val);
                k_head = k_head->next;
            }
        }

        int m_size = m.size();
        if (m_size == 0) return NULL;
        
        mergeSort(m, 0, m_size - 1);

        ListNode* head = new ListNode(m[m_size - 1]);
        ListNode* temp = head;
        m_size -= 2;

        while(m_size >=0 ) {
            temp->next = new ListNode(m[m_size]);
            temp = temp->next;
            --m_size;
        }

        return head;
        
    }

private:
    void merge(std::vector<int> &arr, const int p, const int q, const int r) {
        const int n1 = q - p + 1;
        const int n2 = r - q;

        int L[n1], M[n2];

        for (int i = 0; i < n1; ++i) L[i] = arr[p + i];
        for (int j = 0; j < n2; ++j) M[j] = arr[q + 1 + j];

        int i = 0, j = 0, k = p;

        while (i < n1 && j < n2) arr[k++] = L[i] >= M[j] ? L[i++] : M[j++];

        while (i < n1) arr[k++] = L[i++];

        while (j < n2) arr[k++] = M[j++];
    }

    void mergeSort(std::vector<int> &arr, const int l, const int r) {
        if (l < r) {
            const int m = (r + l) >> 1;

            mergeSort(arr, l, m);
            mergeSort(arr, m + 1, r);

            merge(arr, l, m, r);
        }
    }

};