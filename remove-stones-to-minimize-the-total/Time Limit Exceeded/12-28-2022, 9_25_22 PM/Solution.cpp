// https://leetcode.com/problems/remove-stones-to-minimize-the-total

class Solution {
public:
    int minStoneSum(vector<int>& piles, int k) {
        long unsigned int n = piles.size() - 1;
        for(int i = 0; i < k; i++){
            sort(piles.begin(), piles.end());
            // for(int j = 0; j <= n;j++) cout << piles[j] << " ";
            // cout << endl;
            piles[n] = piles[n] - piles[n]/2;
        }
        int sum = 0;
        for(int i = 0; i <= n;i++){
            sum += piles[i];
            // cout << piles[i] << " ";
        }
        return sum;
    }
};