// https://leetcode.com/problems/perfect-number

class Solution {
public:
    bool checkPerfectNumber(int num) {
        if (n == 1) return false;
        int n = 1;
        for(int i = 2; 2*i <= num; i++ ) n += i * (num % i == 0);
        return n == num;
    }
};