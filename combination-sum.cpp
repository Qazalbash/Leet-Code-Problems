// https://leetcode.com/problems/combination-sum

class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        std::vector<std::vector<int>> res;
        std::vector<int>              subres;
        std::sort(candidates.begin(), candidates.end());

        auto dfs = [&](auto&& self, int target, int start) -> void {
            if (target == 0) {
                res.push_back(subres);
                return;
            }
            for (uint64_t i = start; i < candidates.size(); ++i) {
                if (target < candidates[i]) return;
                subres.push_back(candidates[i]);
                self(self, target - candidates[i], i);
                subres.pop_back();
            }
        };

        dfs(dfs, target, 0);

        return res;
    }
};