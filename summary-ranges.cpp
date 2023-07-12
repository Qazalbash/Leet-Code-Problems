// https://leetcode.com/problems/summary-ranges

class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> ranges;
        int start, end;
        int i = 0;
        const int n = nums.size();

        while (i < n) {
            start = nums[i];
            while (i + 1 < n && nums[i] + 1 == nums[i+1]) ++i;
            end = nums[i];
            ++i;
            if (start == end) ranges.push_back(to_string(start));
            else ranges.push_back(to_string(start)+"->"+to_string(end));
        }

        return ranges;
    }
};