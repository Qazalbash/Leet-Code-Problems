// https://leetcode.com/problems/merge-intervals

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(),
            intervals.end(),
            [](const vector<int>& a, const vector<int>& b) {
                return a[0] < b[0];
            });
        vector<vector<int>> merged;
        merged.push_back(intervals[0]);
        int i, j, m = 1;
        const int n = intervals.size();
        for(i = 1; i < n; ++i) {
            const vector<int> a = intervals[i];
            for(j=0; j<m; ++j) {
                if (overlap(a, merged[j])) {
                    merged[j] = merge(a, merged[j]);
                    break;
                }
            }
            if (j == m) {
                merged.push_back(a);
                ++m;
            }
        }
        return merged;
    }

private:
    bool overlap(const vector<int>& a, const vector<int>& b) {
        if (a[0] <= b[0]) {
            return (a[1] >= b[0]);
        }
        return (b[1] >= a[0]);
    }

    vector<int> merge(const vector<int>& a, const vector<int>& b) {
        return {min(a[0],b[0]), max(a[1],b[1])};
    }
};