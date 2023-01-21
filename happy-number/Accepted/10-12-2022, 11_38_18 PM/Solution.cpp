// https://leetcode.com/problems/happy-number

class Solution {
public:
    bool isHappy(int n) {
        int d;
        while (n > 9)
        {
            d = 0;
            while (n)
            {
                d += pow(n % 10, 2);
                n = n / 10;
            }
            n = d;
        }
        return (n == 1) | (n == 7);
    }
};