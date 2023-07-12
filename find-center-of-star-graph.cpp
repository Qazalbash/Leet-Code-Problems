// https://leetcode.com/problems/find-center-of-star-graph

class Solution {
public:
    int findCenter(vector<vector<int>>& edges) {
        const int w = edges[0][0], x = edges[0][1], y = edges[1][0], z = edges[1][1];
        if (w == x || w == y || w == z) return w;
        if (x == y || x == z) return x;
        if (y == z) return y;
        return z;
    }
};