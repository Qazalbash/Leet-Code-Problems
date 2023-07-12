// https://leetcode.com/problems/largest-local-values-in-a-matrix

class Solution {
public:
    vector<vector<int>> largestLocal(vector<vector<int>>& grid) {
        const int n = grid.size();
        vector<int> sub_r(0, n-2);
        vector<vector<int>> r(n-2, vector<int>(n-2, 0));

        for(int a=0; a+2 < n; ++a){
            for(int b=0; b+2 < n; ++b){
                int max_ = 0;
                for(int i=a; i-a<3; ++i)
                    for(int j=b; j-b<3; ++j) max_ = max(max_, grid[i][j]);
                r[a][b] = max_;
            }
        }
        return r;
    }
};