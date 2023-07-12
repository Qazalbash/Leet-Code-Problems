// https://leetcode.com/problems/powerful-integers

class Solution {
public:
    vector<int> powerfulIntegers(int x, int y, int bound) {
        if (bound < x && bound < y) return {};
        if (x == 1 && y == 1) {
            if (bound >= 2) return {2};
            return {};
        }
        vector<int> real_pi;
        int i, j;
        if (x == 1 || y == 1) {
            const int ij = max(x, y);
            int i = 1;
            while(i + 1 <= bound) {
                real_pi.push_back(i + 1);
                i *= ij;
            }
            return real_pi;
        }

        set<int> pi;
        const int I = log(bound) / log(x) + 1, J = log(bound) / log(y) + 1;
        for(i = 0 ; i < I ; ++i) {
            for(j = 0 ; j < J ; ++j) {
                const int pi_ = pow(x, i) + pow(y, j);
                if (pi_ <= bound) pi.insert(pi_);
            }
        }
        real_pi.assign(pi.begin(), pi.end());
        return real_pi;
    }
};