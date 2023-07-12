// https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal

class Solution {
public:
    bool areAlmostEqual(string s1, string s2) {
        if (s1 == s2) return true;
        const int n = s1.size();
        vector<int> index;
        int i = 0;
        while (i < n) {
            if (s1[i] ^ s2[i]) index.push_back(i);
            ++i;
        }
        
        if (index.size() == 0) return true;
        if(index.size() == 2) {
            i = index[0];
            int j = index[1];
            if (s1[i] ^ s2[j] || s1[j] ^ s2[i]) return false;
            return true;
        }
        return false;
    }
};