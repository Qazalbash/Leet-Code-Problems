// https://leetcode.com/problems/find-the-difference

class Solution {
public:
    char findTheDifference(string s, string t) {
        map<char, int> count;
        for(const char i: t) {
            ++count[i];
        }
        for(const char i: s) {
            --count[i];
        }
        for(const pair<char, int> i: count) {
            if (i.second == 1) {
                return i.first;
            }
        }
        return NULL;
    }
};