// https://leetcode.com/problems/min-cost-climbing-stairs

class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        const size_t n = cost.size();
        for(size_t i = 2 ; i < n ; ++i)
        {
            cost[i] += min(cost[i-1], cost[i-2]);
        }
        return min(cost[n-1], cost[n-2]);
    }
};