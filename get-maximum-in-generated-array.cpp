// https://leetcode.com/problems/get-maximum-in-generated-array

class Solution {
public:
    int getMaximumGenerated(int n) {
        if (n<2) return n;
        int array[n+1];
        array[0] = 0;
        array[1] = 1;
        int max_ele = 0;
        for(int i = 2; i <= n; i++) {
            if(i % 2) array[i] = array[(i-1)/2] + array[(i+1)/2];
            else array[i] = array[i/2];

            if (array[i] > max_ele) max_ele = array[i];
        }
        return max_ele;
    }
};