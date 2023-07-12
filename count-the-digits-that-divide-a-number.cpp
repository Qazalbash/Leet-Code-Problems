// https://leetcode.com/problems/count-the-digits-that-divide-a-number

class Solution {
public:
    int countDigits(int num) {
        // int m = log10(num);
        // m = pow(10, m) > num ? m - 1 : m;
        int digit, total = 0, n_ = num;
        // for (int i = 0; i <= m; ++i) {
        while (n_) {
            digit = n_ % 10;
            n_ /= 10;
            if (num % digit == 0) ++total;
        }
        return total;
    }
};