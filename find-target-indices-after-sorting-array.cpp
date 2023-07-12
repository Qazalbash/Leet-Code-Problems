// https://leetcode.com/problems/find-target-indices-after-sorting-array

class Solution {
public:
    vector<int> targetIndices(vector<int>& nums, int target) {
        map<int, int> counts;
        
        for(const int n: nums) counts[n]++;
        
        int current = target - 1, offset = 0;
        
        while (current > 0) {
            map<int, int>::const_iterator pos = counts.find(current);
            if (pos != counts.end()) {
                offset += pos->second;
            }
            --current;
        }

        const int n = counts[target];

        vector<int> result;

        for( int i = 0; i < n; ++i ) {
            result.push_back(offset + i);
        }
        return result;
    }
};