// https://leetcode.com/problems/base-7

class Solution {
public:
    string convertToBase7(int num) {
        if (num < 7 && num >= 0) return to_string(num);
        const bool is_positive = num > 0;
        num = abs(num);
        string r = "";
        while (num) {
            r = to_string(num % 7) + r;
            num /= 7;
        }
        if (is_positive) return r;
        return "-"+r;
    }
};