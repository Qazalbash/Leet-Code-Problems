// https://leetcode.com/problems/contains-duplicate

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        map<int, uint32_t> m;
        for(int i: nums) {
            if(m[i] > 0) return true;
            m[i] = 1;
        }
        return false;
    }
};