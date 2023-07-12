// https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer

class Solution {
public:
    int subtractProductAndSum(int n) {
        int jama = 0, zarrab = 1;
        while(n) {
            const int digit = n % 10;
            jama+=digit;
            zarrab *= digit;
            n /= 10;
        }
        return (zarrab - jama);
        
    }
};