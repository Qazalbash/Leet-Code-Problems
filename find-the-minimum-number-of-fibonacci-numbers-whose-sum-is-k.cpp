// https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k

class Solution {
public:
    int findMinFibonacciNumbers(int k) {
        vector<int> fibs = {1, 1};
        int i = 1;
        while (fibs[i] + fibs[i-1] <= k) {
            fibs.push_back(fibs[i] + fibs[i-1]);
            ++i;
        }
        
        k = k - fibs[i];
        int count = 1;

        while (k) {
            i = binary_search(i - 1, k, fibs);
            k = k - fibs[i];
            ++count;
        }
        return count;
    }

private:
    int binary_search(int right, const int target, const vector<int>& array) {
        int left = 0, mid;
        while(left <= right) {
            mid = (left + right) >> 1;
            if (array[mid] <= target ) left = mid + 1;
            else right = mid - 1;
        }
        return right;
    }
};