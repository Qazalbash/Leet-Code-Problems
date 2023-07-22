// https://leetcode.com/problems/sort-the-people

class Solution {
public:
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        vector<tuple<string, int>> all;
        const int n = names.size();
        int i = 0;
        for(; i < n; ++i) all.push_back({names[i], heights[i]});

        sort(all.begin(), all.end(), [](const tuple<string, int>& a, const tuple<string, int>& b){
            return get<1>(a) > get<1>(b);
        });

        vector<string> r;
        r.reserve(n);

        std::transform(all.begin(), all.end(), std::back_inserter(r),
                   [](const std::tuple<std::string, int>& tuple) {
                       return std::get<0>(tuple);
                   });

        return r;
    }
};