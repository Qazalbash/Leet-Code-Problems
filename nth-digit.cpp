// https://leetcode.com/problems/nth-digit

class Solution {
public:
    int findNthDigit(int n) {
        if (n < 10) return n;
        long new_n = (long)n;
        long k = 1, p;
        while(true) {
            p = pow(10l, k - 1);
            const long i = new_n - 9 * k * p;
            if (i <= 0) break;
            new_n = i;
            ++k;
        }
        const long digit = (new_n % k) ? k - new_n % k : 0;
        new_n = p + new_n / k - (digit == 0);
        // cout << new_n << " " << digit << endl;
        new_n /= pow(10, digit);
        return new_n % 10;
    }
};