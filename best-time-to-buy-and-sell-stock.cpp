// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0, buy = prices[0];
        for (const int x: prices) {
            buy = min(buy, x);
            profit = max(profit, x - buy);
        }
        return profit;
    }
};