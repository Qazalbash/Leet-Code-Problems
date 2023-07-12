// https://leetcode.com/problems/is-subsequence

class Solution {
public:
    bool isSubsequence(string s, string t) {
        const int ns = s.size(), nt = t.size();
        int ps = 0, pt = 0;
        while ( ps < ns && pt < nt) {
            if (s[ps] == t[pt]) ++ps;
            ++pt;
        }
        return (ps == ns);
    }
};