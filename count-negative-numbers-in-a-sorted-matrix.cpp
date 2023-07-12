// https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix

class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        const int R = grid.size(), C = grid[0].size();
        int neg = 0, r = 0, c;
        for ( ; r < R ; ++r ) {
            c = C - 1;
            while (0 <= c && grid[r][c] < 0) {
                ++neg;
                --c;
            }
        }
        return neg;
    }
};