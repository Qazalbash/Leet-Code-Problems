// https://leetcode.com/problems/sliding-window-maximum

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        const int n = nums.size();
        if (n == 1 || k == 1) return nums;
        vector<int> output;
        deque<int> q;
        int l = 0, r = 0;

        while (r < n) {
            while (!q.empty() && nums[q.back()] < nums[r]) {
                q.pop_back();
            }
            q.push_back(r);
            if (l > q.front()) {
                q.pop_front();
            }
            if ((r+1)>=k) {
                output.push_back(nums[q.front()]);
                ++l;
            }
            ++r;
        }
        return output;
    }
};