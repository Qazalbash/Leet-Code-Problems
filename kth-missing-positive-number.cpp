// https://leetcode.com/problems/kth-missing-positive-number

class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        int i = 1, j = 0;
        const int n = arr.size();
        while(j < n && k) {
            while (i < arr[j] && k) {
                ++i;
                --k;
            }
            if (k) {
                ++j;
                ++i;
            }
        }
        // /if (k)
        return k + i - 1;
        // return i;
    }
};