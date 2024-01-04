// https://leetcode.com/problems/zigzag-conversion

class Solution {
public:
    string convert(string s, int n) {
        const int N = s.size();
        if (n == 1 || N == 1) {
            return s;
        }
        const int R = 2 * (n - 1);
        vector<string> zig(n, "");
        int index = 0;
        int step = -1;
        for(int i = 0; i < N; ++i) {
            zig[index] += s[i];
            if (index == 0) {
                step = 1;
            } else if (index + 1 == n) {
                step = -1;
            }
            index += step;
        }

        return accumulate(zig.begin(), zig.end(), string(""));
    }
};