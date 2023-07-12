// https://leetcode.com/problems/insert-interval

class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        intervals.push_back(newInterval);
        sort(intervals.begin(),
            intervals.end(),
            [&](const vector<int>& a, const vector<int>& b) {
                return a[0] < b[0];
            });
        vector<vector<int>> merged;
        merged.push_back(intervals[0]);
        int j, m = 1;
        const int n = intervals.size();
        for(int i = 1; i < n; ++i) {
            const vector<int> a = intervals[i];
            
            j = 0;
            
            while(j < m && !overlap(a, merged[j])) ++j;
            
            if (j == m) {
                merged.push_back(a);
                ++m;
            } else {
                merged[j] = merge(a, merged[j]);
            }
        }

        return merged;
    }

private:
    bool overlap(const vector<int>& a, const vector<int>& b) {
        return (a[0] <= b[0] && a[1] >= b[0]) || (a[0] > b[0] && b[1] >= a[0]);
    }

    vector<int> merge(const vector<int>& a, const vector<int>& b) {
        return {min(a[0], b[0]), max(a[1], b[1])};
    }
};