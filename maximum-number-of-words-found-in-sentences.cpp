// https://leetcode.com/problems/maximum-number-of-words-found-in-sentences

class Solution {
public:
    int mostWordsFound(vector<string>& sentences) {
        sort(sentences.begin(),
        sentences.end(),
        [](const string& a, const string& b) -> bool {
            return a.size() > b.size();
        });
        int maxcount = 0;
        for(const string& s: sentences) {
            const int count = std::count(s.begin(), s.end(), ' ') + 1;
            maxcount = std::max(maxcount, count);
        }
        return maxcount;
    }
};